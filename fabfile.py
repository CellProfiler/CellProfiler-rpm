# Fabric file that connects to a fresh virtual machine, sets up build
# dependencies, runs the build, and copies out the product and any
# error messages.
#
# During development, run with the IP address of the virtual machine
# in the -H parameter. Example: fab -H 192.168.194.177 build
#

from fabric.api import env, settings, run, put, get, local
from fabric.decorators import with_settings
from fabric.contrib.project import rsync_project

env.user = "cpbuild"

@with_settings(user="root")
def set_up_user(username):
    home = '/home/' + username
    d = dict(home=home, username=username)
    run("""test -d {home} || adduser {username}""".format(**d))
    run("""test -d {home}/.ssh || sudo -u {username} mkdir -m 700 {home}/.ssh""".format(**d))
    put("ssh_keys/id_rsa.pub", "{home}/.ssh/authorized_keys".format(**d), mode=0600)
    run("""chown {username}:{username} {home}/.ssh/authorized_keys""".format(**d))
    run("""echo '{username}	ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers""".format(**d))

def build():
    set_up_user("cpbuild")
    local("tar cpf workspace.tar --exclude workspace.tar ..")
    put("workspace.tar")
    put("build_cellprofiler.sh", "~", mode=0755)
    run("./build_cellprofiler.sh")
    get("cellprofiler.tar.gz", "cellprofiler.tar.gz")

def deploy():
    with settings(user="root"):
        run("yum -y install gtk2-devel mesa-libGL mesa-libGL-devel blas atlas lapack blas-devel atlas-devel lapack-devel xorg-x11-xauth* xorg-x11-xkb-utils* qt-devel openssl openssl-devel xclock *Xvfb* svn libXtst")
        put("cellprofiler.tar.gz")
        run("tar -C / -xzf cellprofiler.tar.gz")

def test():
    set_up_user("johndoe")
    deploy()
    with settings(user="johndoe"):
        run("/usr/CellProfiler/CellProfiler/shortcuts/cellprofiler -t")

#
# Build RPMs
#

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
    epackages with restore_state.

    """
    run("rpm -qa | sort > /root/rpmstate")

@with_settings(user="root")
def restore_state():
    run("rpm -qa | sort > /tmp/rpmstate")
    run("diff /root/rpmstate /tmp/rpmstate |grep ^\> |cut -c3- > /tmp/to_erase")
    run("test -s /tmp/to_erase && xargs rpm -e < /tmp/to_erase || true")

@with_settings(user="root")
def deploy_build_machine():
    set_up_user("cpbuild")
    run("yum install -q -y rpm-build yum-utils createrepo rsync")
    run("mkdir -p /root/repo")
    run("createrepo /root/repo")
    run("chmod -R o-w+r /root/repo")
    put("root-repo.repo", "/etc/yum.repos.d/root.repo")
    save_state()
    
def rsync_sources():
    run("mkdir -p rpmbuild/SOURCES")
    rsync_project("rpmbuild/SOURCES/", "~/research/cpbuild/SOURCES/")

def rsync_rpms():
    run("mkdir -p rpmbuild/RPMS")
    rsync_project("rpmbuild/RPMS/", "~/research/cpbuild/RPMS/")
    with settings(user="root"):
        run("rm -rf /root/repo")
        run("cp -r ~cpbuild/rpmbuild/RPMS/x86_64/ /root/repo")
        run("createrepo /root/repo")

def build_rpm(basename):
    restore_state()
    run("rm -rf rpmbuild/RPMS")
    run("rm -rf rpmbuild/BUILD")
    run("mkdir -p rpmbuild/SPECS")
    put("SPECS/%s.spec" % basename, "rpmbuild/SPECS/")
    with settings(user="root"):
        run("yum-builddep -q -y ~cpbuild/rpmbuild/SPECS/%s.spec" % basename)
    run("rpmbuild -ba rpmbuild/SPECS/%s.spec" % basename)
    get("rpmbuild/RPMS/x86_64/*.rpm", "~/research/cpbuild/RPMS/x86_64/")
    with settings(user="root"):
        run("cp ~cpbuild/rpmbuild/RPMS/x86_64/*.rpm /root/repo")
        run("createrepo /root/repo")
        run("yum makecache")

def maybe_build_rpm(basename):
    """
    Build an RPM only if we don't have it here. This function exists
    only so we can run build_all_rpms several times while fixing bugs
    and get Make-like behavior.

    """
    res = local("ls RPMS/x86_64 | grep '^%s-[^-]*-[^-]*\.x86_64\.rpm$' || true" % basename, capture=True)
    if res == "":
        print "Building", basename
        build_rpm(basename)
    else:
        print "Not building", basename

def build_all_rpms():
    rsync_sources()
    rsync_rpms()
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
            'cellprofiler-h5py',
            'cellprofiler-swig',
            'cellprofiler-pyopengl',
            'cellprofiler-pyopengl-accelerate',
            'cellprofiler-wxpython2.8-gtk2-unicode',
            'cellprofiler-dateutil',
            'cellprofiler-pytz',
            'cellprofiler-six',
            'cellprofiler-matplotlib',
            'cellprofiler-scipy',
            'cellprofiler-sip',
            'cellprofiler-pyqt-x11-gpl',
            'cellprofiler-qimage2ndarray',
            'cellprofiler-vigra',
            'cellprofiler-ilastik',
            'cellprofiler-pyzmq',
            'cellprofiler-cython',
            'cellprofiler-jdk',
            'cellprofiler'
    ]:
        maybe_build_rpm(basename)

@with_settings(user="root")
def deploy_test_machine():
    run("yum -y update")
    set_up_user("johndoe")
    run("yum install -q -y xauth")
    put("public-centos6.repo", "/etc/yum.repos.d/cellprofiler.repo")
    save_state()

@with_settings(user="root")
def install_cp():
    restore_state()
    run("yum makecache")
    run("yum -y install cellprofiler")

