%define pkgname cellprofiler-pyzmq
%define pyversion 2.7
%define version 13.1.0
%define release 1
%define tarname pyzmq
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pyzmq installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD or LGPL
URL:       http://github.com/zeromq/pyzmq
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python gcc gcc-c++

%description
pyzmq installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/zmq
%{pref}/lib/python2.7/site-packages/pyzmq-13.1.0-py2.7.egg-info
