# Fabric file that connects to a fresh virtual machine, sets up build
# dependencies, runs the build, and copies out the product and any
# error messages.
#
# During development, run with the IP address of the virtual machine
# in the -H parameter. Example: fab -H 192.168.194.177 build
#

import os.path
import urllib2
import json
import re
import datetime
from StringIO import StringIO
from fabric.api import env, settings, run, put, get, local
from fabric.decorators import with_settings
from fabric.contrib.project import rsync_project

env.user = "cpbuild"
env.use_ssh_config = True

# The linux_repositories directory
basedir = os.path.dirname(__file__)

@with_settings(user="root")
def set_up_user(username):
    home = '/home/' + username
    d = dict(home=home, username=username)
    run("""test -d {home} || adduser {username}""".format(**d))
    run("""test -d {home}/.ssh || sudo -u {username} mkdir -m 700 {home}/.ssh""".format(**d))
    put(os.path.join(basedir, "ssh_keys", "id_rsa.pub"),
        "{home}/.ssh/authorized_keys".format(**d), mode=0600)
    run("""chown {username}:{username} {home}/.ssh/authorized_keys""".format(**d))
    run("""echo '{username}	ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers""".format(**d))

@with_settings(user="root")
def set_hostname(new_hostname):
    """
    Set the hostname of a newly deployed virtual machine. This isn't
    necessary.

    """
    run("sed -i.bak 's/HOSTNAME=.*/HOSTNAME=%s/' /etc/sysconfig/network" % new_hostname)
    run("hostname %s" % new_hostname)
    run("/etc/init.d/network restart")

@with_settings(user="root")
def save_state():
    """
    Save a list of installed RPMs so we can return to this set of
    packages with restore_state.

    """
    run("rpm -qa | sort > /root/rpmstate")

@with_settings(user="root")
def restore_state():
    """Remove any RPMs that have been installed since save_state()."""
    run("""if [ -f /root/rpmstate ]; then
             rpm -qa | sort > /tmp/rpmstate;
             diff /root/rpmstate /tmp/rpmstate | grep ^\> | cut -c3- > /tmp/to_erase;
             if [ -s /tmp/to_erase ]; then
               xargs rpm -e < /tmp/to_erase;
             fi;
           fi""")

@with_settings(user="root")
def _deploy(username, packages):
    restore_state()
    run("yum -y update")
    run("yum install -q -y {packages}".format(packages=packages))
    set_up_user(username)
    run("rm -rf /root/repo")
    run("mkdir /root/repo")
    run("createrepo /root/repo")
    run("chmod -R o-w+r /root/repo")
    put(os.path.join(basedir, "root.repo"), "/etc/yum.repos.d/root.repo")
    save_state()

@with_settings(user="root")
def deploy_build_machine():
    """
    Prepare a fresh machine for build RPMs. Creates a cpbuild user,
    installs necessary packages, and sets up a local repository on
    the build machine..

    """
    _deploy("cpbuild", "rpm-build yum-utils createrepo rsync sudo tar")

def _port_string(env):
    """Incantation to convince rsync to use a different port."""
    if env.port is None:
        return ''
    else:
        return "-e 'ssh -p {port}'".format(port=env.port)
 
@with_settings(user="cpbuild")
def push_sources():
    """
    Copy the sources to the build machine. Deletes anything that shouldn't
    be there, ensuring that the directory on the build machine contains
    the same as our local SOURCES directory.

    """
    run("mkdir -p rpmbuild/SOURCES")
    local("rsync -avz {port_string} --delete {basedir}/SOURCES/ cpbuild@{host}:rpmbuild/SOURCES/".format(basedir=basedir, host=env.host, port_string=_port_string(env)))

@with_settings(user="root")
def push(source="."):
    """
    Copies all the RPMs in the current directory to the repository on the
    remote machine (either a build machine or a test machine). Deletes any
    RPMs that shouldn't be there, ensuring that the directories contain the
    same RPMs.

    """
    local("rsync -avz {port_string} --include='*.rpm' --exclude='*' --delete . root@{host}:/root/repo/".format(host=env.host, port_string=_port_string(env)))
    rsync_project("/root/repo/", source)
    run("createrepo /root/repo")
    run("chmod -R o-w+r /root/repo")
    run("yum makecache")

@with_settings(user="root")
def pull():
    """
    Copies all the RPMs in the repository on the build machine to the
    current directory on the local machine. Deletes any RPMs that shouldn't
    be here, ensuring that the directories contain the same RPMs.

    """
    local("rsync -avz {port_string} --include='*.rpm' --exclude='*' --delete root@{host}:/root/repo/ .".format(host=env.host, port_string=_port_string(env)))

def build_rpm(basename):
    """
    Builds an RPM. First uninstall packages in order to restore the build
    machine to its freshly deployed state. After the build succeeds, this
    task copies the resulting RPM(s) to the repository on the build machine.
    You will need to use the "pull" task to retrieve it.

    This task copies the local .spec file to the build machine before
    building, but you will have to copy the sources over by running the task
    push_sources() before starting the build.

    """
    restore_state()
    run("rm -rf rpmbuild/RPMS")
    run("rm -rf rpmbuild/BUILD")
    run("mkdir -p rpmbuild/SPECS")
    put(os.path.join(basedir, "SPECS", "%s.spec" % basename), "rpmbuild/SPECS/")
    with settings(user="root"):
        run("yum-builddep -q -y ~cpbuild/rpmbuild/SPECS/%s.spec" % basename)
    run("rpmbuild -ba rpmbuild/SPECS/%s.spec" % basename)
    with settings(user="root"):
        run("cp ~cpbuild/rpmbuild/RPMS/*/*.rpm /root/repo/")
        run("createrepo /root/repo")
        run("yum makecache")

def maybe_build_rpm(basename):
    """
    Build an RPM only if we don't have it here. This function exists
    only so we can run build_all_rpms several times while fixing bugs
    and get Make-like behavior.

    """
    res = local("ls *.rpm | grep '^%s-[^-]*-[^-]*\.x86_64\.rpm$' || true" % basename, capture=True)
    if res == "":
        print "Building", basename
        build_rpm(basename)
    else:
        print "Not building", basename

def maybe_build_all_rpms():
    """
    Build CellProfiler and all of its dependencies in the correct order.
    This calls maybe_build_rpm(), so it will skip RPMs that are already
    here.

    """
    for basename in [
            'cellprofiler-zlib',
            'cellprofiler-sqlite',
            'cellprofiler-python',
            'cellprofiler-setuptools',
            'cellprofiler-decorator',
            'cellprofiler-hdf5',
            'cellprofiler-libjpeg',
            'cellprofiler-libpng',
            'cellprofiler-libtiff',
            'cellprofiler-pil',
            'cellprofiler-pysqlite',
            'cellprofiler-mysqlpython',
            'cellprofiler-umfpack',
            'cellprofiler-numpy',
            'cellprofiler-cython',
            'cellprofiler-h5py',
            'cellprofiler-swig',
            'cellprofiler-pyopengl',
            'cellprofiler-pyopengl-accelerate',
            'cellprofiler-wxpython2.8-gtk2-unicode',
            'cellprofiler-dateutil',
            'cellprofiler-pytz',
            'cellprofiler-six',
            'cellprofiler-matplotlib',
			'cellprofiler-pandas',
            'cellprofiler-scipy',
            'cellprofiler-sip',
            'cellprofiler-pyqt-x11-gpl',
            'cellprofiler-qimage2ndarray',
            'cellprofiler-vigra',
            'cellprofiler-ilastik',
            'cellprofiler-pyzmq',
            'cellprofiler-jdk',
            'cellprofiler-javabridge',
            'cellprofiler-bioformats',
            'cellprofiler-scikit-learn',
            'cellprofiler'
    ]:
        maybe_build_rpm(basename)

def use_public_repo():
    with settings(user='root'):
        put(os.path.join(basedir, "public-centos6.repo"), "/etc/yum.repos.d/cellprofiler.repo")

def build_cellprofiler_only():
    """Builds an RPM of just CellProfiler.

    Fulfills the dependencies using the RPMs that have already been
    made public.

    """
    use_public_repo()
    deploy_build_machine()
    push_sources()
    run("cd rpmbuild/SOURCES; curl -s -L -O https://github.com/CellProfiler/CellProfiler/archive/0c7fb94.tar.gz")
    build_rpm("cellprofiler")
    pull()

def build_cellprofiler_version(commit, token):
    """Builds an RPM for a particular version of CellProfiler

    commit - the Git hash tag of the commit
    token - an OAuth personal access token from github

    Go to https://github.com/settings/applications to generate one
    """
    restore_state()
    run("rm -rf rpmbuild/RPMS")
    run("rm -rf rpmbuild/BUILD")
    run("mkdir -p rpmbuild/SPECS")
    tag, count, commit_sha = _github_describe(
        "CellProfiler", "CellProfiler", commit, token)
    print "Using tag=%s, count=%d, commit=%s" % (tag, count, commit_sha)
    use_public_repo()
    deploy_build_machine()
    push_sources()
    run("curl -s -L -o rpmbuild/SOURCES/cellprofiler-%s.tar.gz https://github.com/CellProfiler/CellProfiler/archive/%s.tar.gz" % (commit, commit_sha))
    spec = _get("https://github.com/CellProfiler/CellProfiler/raw/%s/jenkins/linux/cellprofiler-centos6.spec" % commit_sha)
    if tag.endswith("-SNAPSHOT"):
        tag = tag[:-len("-SNAPSHOT")]
        snapshot = "SNAPSHOT"
    else:
        snapshot = ""
    today = datetime.date.today()
    release = "0.%d%02d%02dgit%s%s" % (today.year, today.month, today.day,
                                       commit_sha[:10], snapshot)
    #
    # First, replace the tarball name with the name that's downloaded
    #
    spec = spec.replace("%define tarname cellprofiler",
                        "%%define tarname cellprofiler-%s" % commit)
    #
    # Then, replace the %setup command with one that anticipates
    # where the tarball will spew
    #
    spec = spec.replace(
        "%setup -q -n CellProfiler",
        "%%setup -q -n CellProfiler-%s" % commit_sha)
    parts = ["%%define version %s.%d" % (tag, count),
             "%%define release %s" % release,
             spec]
    spec = "\n".join(parts)
    put(local_path=StringIO(spec), 
        remote_path="rpmbuild/SPECS/cellprofiler-%s.spec" % commit)
    with settings(user="root"):
        run("yum-builddep -q -y ~cpbuild/rpmbuild/SPECS/cellprofiler-%s.spec" % commit)
    run("rpmbuild -ba rpmbuild/SPECS/cellprofiler-%s.spec" % commit)
    with settings(user="root"):
        run("cp ~cpbuild/rpmbuild/RPMS/*/*.rpm /root/repo/")
        run("createrepo /root/repo")
        run("yum makecache")
    pull()

def deploy_test_machine():
    """
    Prepare a fresh machine for testing CellProfiler. Creates a johndoe
    user, installs necessary packages, and sets up a local repository on
    the test machine.

    You will need to copy the RPMs to the test machine with push()
    and then install CellProfiler with install_cp().

    """
    _deploy("johndoe", "xauth rsync createrepo unzip sudo")

@with_settings(user="root")
def install_cp():
    """
    Install CellProfiler and all its dependencies. First, it tries to
    restore the test machine to its freshly deployed state so that
    all the packages will be reinstalled.

    """
    restore_state()
    run("yum makecache")
    run("yum -y install cellprofiler")

@with_settings(user="root")
def test_public_cp_centos():
    run("yum -y update")
    run("yum install -q -y xauth sudo")
    set_up_user("johndoe")
    use_public_repo()
    run("yum makecache")
    run("yum -y install cellprofiler")

def _github_describe(owner, repo, commit, token):
    """Perform a git describe via the github URL
    
    owner - name of the repository owner on Github
    repo - name of the repository
    commit - the Git hash of the commit
    token - the OAUTH access token that gives us unlimited use of the api
    
    returns a tuple of tag name, commits past the tag and the full GIT hash
    
    if there is no tag among the parents, 
    """
    tags = _make_request(owner, repo, token, "tags")
    tags = dict([(tag["commit"]["sha"], tag) for tag in tags])
    current_commit = _make_request(owner, repo, token, "commits", commit)
    commit_sha = current_commit["sha"]
    def describe_fn(owner, repo, current_commit):
        sha = current_commit["sha"]
        if sha in tags:
            tag = tags[sha]
            return tag["name"], 0
        parents = current_commit["parents"]
        for parent in parents:
            parent_commit = _make_request(owner, repo, token, "commits", parent["sha"])
            tag, count = describe_fn(owner, repo, parent_commit)
            if tag is not None:
                return tag, count+1
        return None, None
    tag, count = describe_fn(owner, repo, current_commit)
    return tag, count, commit_sha

def _make_request(owner, repo, token, *args):
    url = "https://api.github.com/repos/%s/%s/" % (owner, repo)
    url += "/".join(args)
    url += "?access_token=%s"%token
    data = _get(url)
    return json.loads(data)

def _get(url):
    fd = urllib2.urlopen(url)
    data = ""
    while True:
        part = fd.read()
        if len(part) == 0:
            break
        data += part
    fd.close()
    return data
