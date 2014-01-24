This document describes the setup for building Linux packages (RPMs) of
CellProfiler and its dependencies and publishing them on the web.

SSH is set up to allow logging into the build machines without
paswords, but there have been some problems with this due to a CentOS
6 bug. If you are asked for a password, you can find it on the
Passwords wiki page. Then, run `restorecon -R -v /root/.ssh` to make
password-less login work on CentOS 6.


## Files and directories

fabfile.py
: Fabric tasks for building and testing.

htdocs/linux
: This is the directory that is exposed on the web. It contains a subdirectory
: for each Linux distribution. For RPM-based distributions such as CentOS, that
: directory is a yum repository created by createrepo (see below).

ssh_keys
: Contains SSH keys that are installed on the build and test machines by some
: of the fabric tasks.

SPECS
: RPM spec files.


## How to rebuild only CellProfiler

 0. Edit SPECS/cellprofiler.spec and update the version, release, and/or
    tarname. The tarname should be the git hash. Example:

    %define version 2.1.0.Release
    %define release 1
    %define tarname 0c7fb94

 1. Activate the virtualenv.

    . venv/bin/activate

 2. Make a working directory. This directory will contain RPMs as you build
    them and test; you will finally copy them to the website.

    $ mkdir foo
    $ cd foo

 3. Start a clean build machine by going to http://broad.io/imagingcloud,
    logging in, and add a vApp based on the template "Cent OS 6 x64" in
    the Build Catalog.

 4. Wait for the build machine to start and get its IP address,
    192.168.195.XXX.

 5. Upgrade the operating system and install packages needed to build.
 
    $ fab -H 192.168.195.XXX deploy_build_machine

 6. Build the cellprofiler RPM.

    $ fab -H 192.168.195.XXX build_cellprofiler_only

 7. Start a clean test machine by going to http://broad.io/imagingcloud,
    logging in, and add a vApp based on the template "Cent OS 6 x64" in
    the Build Catalog.

 8. Wait for the test machine to start and get its IP address, 192.168.195.YYY.

 9. Upgrade the operating system and install packages needed to test.

    $ fab -H 192.168.195.YYY deploy_test_machine

10. Tell the test machine to get the dependencies from the public repository.

    $ fab -H 192.168.195.YYY use_public_repo

11. Copy the new RPM to the test machine.

    $ fab -H 192.168.195.YYY push

13. Install CellProfiler on the test machine.

    $ fab -H 192.168.195.YYY install_cp

    (Not 100% sure that this will get the newly built version and not the
    version that is in the public repository. Check.)

14. Log in and check that it works to start CellProfiler.

    $ ssh -Y johndoe@192.168.195.YYY cellprofiler

15. Add the new RPM files to the public repository.

    $ cp *.rpm ../htdocs/linux/centos6/
    $ createrepo ../htdocs/linux/centos6/

16. Delete the working directory.

    $ cd ..
    $ rm -rf foo


## How to rebuild everything

 0. Activate the virtualenv.

    . venv/bin/activate

 1. Make a working directory. This directory will contain RPMs as you build
    them and test; you will finally copy them to the website.

    $ mkdir foo
    $ cd foo

 2. Start a clean build machine by going to http://broad.io/imagingcloud,
    logging in, and add a vApp based on the template "Cent OS 6 x64" in
    the Build Catalog.

 3. Wait for the build machine to start and get its IP address,
    192.168.195.XXX.

 4. Upgrade the operating system and install packages needed to build.
 
    $ fab -H 192.168.195.XXX deploy_build_machine

 5. Copy the contents of the SOURCES directory to the build machine.

    $ fab -H 192.168.195.XXX push_sources

 6. Build all the RPMs.

    $ fab -H 192.168.195.XXX maybe_build_all_rpms

 7. If something won't build, modify the .spec file as needed and repeat
    step 6 until it works. If you add a file to SOURCES, run step 5 again.

 8. Copy all the RPMs from the build machine.

    $ fab -H 192.168.195.XXX pull

 9. Start a clean test machine by going to http://broad.io/imagingcloud,
    logging in, and add a vApp based on the template "Cent OS 6 x64" in
    the Build Catalog.

10. Wait for the test machine to start and get its IP address, 192.168.195.YYY.

11. Upgrade the operating system and install packages needed to test.

    $ fab -H 192.168.195.YYY deploy_test_machine

12. Copy the RPMs to the test machine.

    $ fab -H 192.168.195.YYY push

13. Install CellProfiler on the test machine.

    $ fab -H 192.168.195.YYY install_cp

14. Log in and start CellProfiler.

    $ ssh -Y johndoe@192.168.195.YYY cellprofiler

15. Add the new RPM files to the public repository.

    $ cp *.rpm ../htdocs/linux/centos6/
    $ createrepo ../htdocs/linux/centos6/

16. Delete the working directory.

    $ cd ..
    $ rm -rf foo


## Reindexing a yum repository

After adding or removing RPM files from a yum repository, run createrepo 
in order to recreate the index files. For instance:

    createrepo htdocs/linux/centos6


## Testing CellProfiler

    fab -H 192.168.195.XXX deploy_test_machine
    fab -H 192.168.195.XXX install_cp


## How the virtualenv was made

The directory venv is a python virtualenv that contains software needed
to start builds and create repositories. The virtualenv was made as
follows:

1. Create virtualenv

    virtualenv --prompt='(linux_repositories)' venv

2. Activate virtualenv

    . venv/bin/activate

3. Install createrepo

    mkdir venv/src
    cd venv/src
    wget http://createrepo.baseurl.org/download/createrepo-0.3.6.tar.gz
    tar xzf createrepo-0.3.6.tar.gz
    cd createrepo-0.3.6
    patch < ../../../createrepo-sysconfdir.patch
    make prefix=$(dirname $(dirname $(pwd))) install
    cd ../../..
    # ManuallyrReplace /usr/share with $(dirname $(dirname "$0")) in
    # venv/bin/createrepo.

4. Install fabric

    pip install fabric



