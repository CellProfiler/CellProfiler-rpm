%define pkgname cellprofiler-numpy
%define version 1.5.1
%define release 1
%define tarname numpy
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   numpy
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://numeric.scipy.org/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-umfpack fftw lapack atlas blas
BuildRequires: cellprofiler-python cellprofiler-umfpack-devel fftw-devel gcc-gfortran lapack-devel atlas-devel blas-devel

%description
numpy installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   numpy development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
numpy development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

#cp site.cfg.example site.cfg
#perl -pi -e 's@#(\[DEFAULT\])@$1@g' site.cfg
#perl -pi -e 's@#(library_dirs.*)@$1:/usr/lib64/atlas:%{pref}/lib@g' site.cfg
#perl -pi -e 's@#(include_dirs.*)@$1:/usr/include/atlas:%{pref}/include@g' site.cfg
#perl -pi -e 's@#(\[lapack_opt\])@$1@g' site.cfg
#perl -pi -e 's@#(libraries = .*)@libraries = clapack, lapack, gfortran@g' site.cfg
#perl -pi -e 's@#(\[amd\])@$1@g' site.cfg
#perl -pi -e 's@#(amd_libs)@$1@g' site.cfg
#perl -pi -e 's@#(\[umfpack\])@$1@g' site.cfg
#perl -pi -e 's@#(umfpack_libs)@$1@g' site.cfg
#perl -pi -e 's@#(\[fftw\])@$1@g' site.cfg
#perl -pi -e 's@#(libraries = fftw3)@$1@g' site.cfg
#perl -pi -e 's@#(\[djbfft\])@$1@g' site.cfg

env ATLAS=/usr/lib64/atlas FFTW=%{pref}/lib BLAS=/usr/lib64/atlas \
    LAPACK=/usr/lib64/atlas CFLAGS="$RPM_OPT_FLAGS" \
%{pref}/bin/python setup.py build --fcompiler=gfortran 


%install

#%{pref}/bin/python setup.py install --skip-build --root $RPM_BUILD_ROOT
env ATLAS=/usr/lib64/atlas FFTW=%{pref}/lib BLAS=/usr/lib64/atlas \
    LAPACK=/usr/lib64/atlas CFLAGS="$RPM_OPT_FLAGS" \
    %{pref}/bin/python setup.py install --root $RPM_BUILD_ROOT

#cd $RPM_BUILD_ROOT%{pref}/lib/python2.7/site-packages/numpy/distutils
#perl -pi -e 's@#(\[DEFAULT\])@$1@g' site.cfg
#perl -pi -e 's@#(library_dirs.*)@$1:%{pref}/lib@g' site.cfg
#perl -pi -e 's@#(include_dirs.*)@$1:%{pref}/include@g' site.cfg
#perl -pi -e 's@#(\[lapack_opt\])@$1@g' site.cfg
#perl -pi -e 's@#(libraries = lapack, blas, atlas)@$1, gfortran@g' site.cfg
#perl -pi -e 's@#(\[amd\])@$1@g' site.cfg
#perl -pi -e 's@#(amd_libs)@$1@g' site.cfg
#perl -pi -e 's@#(\[umfpack\])@$1@g' site.cfg
#perl -pi -e 's@#(umfpack_libs)@$1@g' site.cfg
#perl -pi -e 's@#(\[fftw\])@$1@g' site.cfg
#perl -pi -e 's@#(libraries = fftw3)@$1@g' site.cfg
#perl -pi -e 's@#(\[djbfft\])@$1@g' site.cfg

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/f2py
%{pref}/lib/python2.7/site-packages/numpy-1.5.1-py2.7.egg-info
%doc %{pref}/lib/python2.7/site-packages/numpy/COMPATIBILITY
%doc %{pref}/lib/python2.7/site-packages/numpy/DEV_README.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/INSTALL.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/LICENSE.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/README.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/THANKS.txt
%{pref}/lib/python2.7/site-packages/numpy/__config__.py
%{pref}/lib/python2.7/site-packages/numpy/__config__.pyc
%{pref}/lib/python2.7/site-packages/numpy/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/_import_tools.py
%{pref}/lib/python2.7/site-packages/numpy/_import_tools.pyc
%{pref}/lib/python2.7/site-packages/numpy/add_newdocs.py
%{pref}/lib/python2.7/site-packages/numpy/add_newdocs.pyc
%{pref}/lib/python2.7/site-packages/numpy/compat/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/compat/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/compat/_inspect.py
%{pref}/lib/python2.7/site-packages/numpy/compat/_inspect.pyc
%{pref}/lib/python2.7/site-packages/numpy/compat/py3k.py
%{pref}/lib/python2.7/site-packages/numpy/compat/py3k.pyc
%{pref}/lib/python2.7/site-packages/numpy/compat/setup.py
%{pref}/lib/python2.7/site-packages/numpy/compat/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/compat/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/compat/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/core/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/_internal.py
%{pref}/lib/python2.7/site-packages/numpy/core/_internal.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/_mx_datetime_parser.py
%{pref}/lib/python2.7/site-packages/numpy/core/_mx_datetime_parser.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/_sort.so
%{pref}/lib/python2.7/site-packages/numpy/core/arrayprint.py
%{pref}/lib/python2.7/site-packages/numpy/core/arrayprint.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/defchararray.py
%{pref}/lib/python2.7/site-packages/numpy/core/defchararray.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/fromnumeric.py
%{pref}/lib/python2.7/site-packages/numpy/core/fromnumeric.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/function_base.py
%{pref}/lib/python2.7/site-packages/numpy/core/function_base.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/generate_numpy_api.py
%{pref}/lib/python2.7/site-packages/numpy/core/generate_numpy_api.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/getlimits.py
%{pref}/lib/python2.7/site-packages/numpy/core/getlimits.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/info.py
%{pref}/lib/python2.7/site-packages/numpy/core/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/lib/npy-pkg-config/mlib.ini
%{pref}/lib/python2.7/site-packages/numpy/core/lib/npy-pkg-config/npymath.ini
%{pref}/lib/python2.7/site-packages/numpy/core/machar.py
%{pref}/lib/python2.7/site-packages/numpy/core/machar.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/memmap.py
%{pref}/lib/python2.7/site-packages/numpy/core/memmap.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/multiarray.so
%{pref}/lib/python2.7/site-packages/numpy/core/multiarray_tests.so
%{pref}/lib/python2.7/site-packages/numpy/core/numeric.py
%{pref}/lib/python2.7/site-packages/numpy/core/numeric.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/numerictypes.py
%{pref}/lib/python2.7/site-packages/numpy/core/numerictypes.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/records.py
%{pref}/lib/python2.7/site-packages/numpy/core/records.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/scalarmath.so
%{pref}/lib/python2.7/site-packages/numpy/core/scons_support.py
%{pref}/lib/python2.7/site-packages/numpy/core/scons_support.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/setup.py
%{pref}/lib/python2.7/site-packages/numpy/core/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/setup_common.py
%{pref}/lib/python2.7/site-packages/numpy/core/setup_common.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/core/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/shape_base.py
%{pref}/lib/python2.7/site-packages/numpy/core/shape_base.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/tests/data/astype_copy.pkl
%{pref}/lib/python2.7/site-packages/numpy/core/tests/data/recarray_from_file.fits
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_arrayprint.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_blasdot.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_defchararray.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_dtype.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_errstate.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_function_base.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_getlimits.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_machar.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_memmap.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_multiarray.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_numeric.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_numerictypes.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_print.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_records.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_scalarmath.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_shape_base.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_ufunc.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_umath.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_umath_complex.py
%{pref}/lib/python2.7/site-packages/numpy/core/tests/test_unicode.py
%{pref}/lib/python2.7/site-packages/numpy/core/umath.so
%{pref}/lib/python2.7/site-packages/numpy/core/umath_tests.so
%{pref}/lib/python2.7/site-packages/numpy/ctypeslib.py
%{pref}/lib/python2.7/site-packages/numpy/ctypeslib.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/__config__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/__config__.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/__version__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/__version__.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/ccompiler.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/ccompiler.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/autodist.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/autodist.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/bdist_rpm.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/bdist_rpm.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_clib.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_clib.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_ext.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_ext.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_py.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_py.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_scripts.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_scripts.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_src.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/build_src.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/config.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/config.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/config_compiler.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/config_compiler.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/develop.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/develop.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/egg_info.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/egg_info.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_clib.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_clib.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_data.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_data.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_headers.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/install_headers.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/scons.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/scons.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/sdist.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/command/sdist.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/compat.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/compat.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/conv_template.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/conv_template.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/core.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/core.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/cpuinfo.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/cpuinfo.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/environment.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/environment.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/exec_command.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/exec_command.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/extension.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/extension.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/absoft.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/absoft.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/compaq.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/compaq.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/g95.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/g95.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/gnu.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/gnu.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/hpux.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/hpux.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/ibm.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/ibm.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/intel.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/intel.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/lahey.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/lahey.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/mips.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/mips.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/nag.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/nag.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/none.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/none.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/pg.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/pg.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/sun.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/sun.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/vast.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/fcompiler/vast.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/from_template.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/from_template.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/info.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/intelccompiler.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/intelccompiler.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/interactive.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/interactive.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/lib2def.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/lib2def.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/line_endings.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/line_endings.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/log.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/log.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/mingw/gfortran_vs2003_hack.c
%{pref}/lib/python2.7/site-packages/numpy/distutils/mingw32ccompiler.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/mingw32ccompiler.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/misc_util.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/misc_util.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/npy_pkg_config.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/npy_pkg_config.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/numpy_distribution.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/numpy_distribution.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/system_info.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/system_info.pyc
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_ext/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_ext/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_ext/src/fib1.f
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_ext/src/fib2.pyf
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_ext/tests/test_fib2.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_f90_ext/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_f90_ext/include/body.f90
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_f90_ext/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_f90_ext/src/foo_free.f90
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/f2py_f90_ext/tests/test_foo.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/gen_ext/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/gen_ext/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/gen_ext/tests/test_fib3.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/pyrex_ext/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/pyrex_ext/primes.pyx
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/pyrex_ext/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/pyrex_ext/tests/test_primes.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/setup.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/tests/test_example.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/tests/test_example2.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/test_fcompiler_gnu.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/test_misc_util.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/test_npy_pkg_config.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/unixccompiler.py
%{pref}/lib/python2.7/site-packages/numpy/distutils/unixccompiler.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/doc/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/basics.py
%{pref}/lib/python2.7/site-packages/numpy/doc/basics.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/broadcasting.py
%{pref}/lib/python2.7/site-packages/numpy/doc/broadcasting.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/byteswapping.py
%{pref}/lib/python2.7/site-packages/numpy/doc/byteswapping.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/constants.py
%{pref}/lib/python2.7/site-packages/numpy/doc/constants.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/creation.py
%{pref}/lib/python2.7/site-packages/numpy/doc/creation.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/glossary.py
%{pref}/lib/python2.7/site-packages/numpy/doc/glossary.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/howtofind.py
%{pref}/lib/python2.7/site-packages/numpy/doc/howtofind.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/indexing.py
%{pref}/lib/python2.7/site-packages/numpy/doc/indexing.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/internals.py
%{pref}/lib/python2.7/site-packages/numpy/doc/internals.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/io.py
%{pref}/lib/python2.7/site-packages/numpy/doc/io.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/jargon.py
%{pref}/lib/python2.7/site-packages/numpy/doc/jargon.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/methods_vs_functions.py
%{pref}/lib/python2.7/site-packages/numpy/doc/methods_vs_functions.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/misc.py
%{pref}/lib/python2.7/site-packages/numpy/doc/misc.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/performance.py
%{pref}/lib/python2.7/site-packages/numpy/doc/performance.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/structured_arrays.py
%{pref}/lib/python2.7/site-packages/numpy/doc/structured_arrays.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/subclassing.py
%{pref}/lib/python2.7/site-packages/numpy/doc/subclassing.pyc
%{pref}/lib/python2.7/site-packages/numpy/doc/ufuncs.py
%{pref}/lib/python2.7/site-packages/numpy/doc/ufuncs.pyc
%{pref}/lib/python2.7/site-packages/numpy/dual.py
%{pref}/lib/python2.7/site-packages/numpy/dual.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/__version__.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/__version__.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/auxfuncs.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/auxfuncs.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/capi_maps.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/capi_maps.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/cb_rules.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/cb_rules.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/cfuncs.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/cfuncs.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/common_rules.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/common_rules.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/crackfortran.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/crackfortran.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/diagnose.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/diagnose.pyc
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/FAQ.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/HISTORY.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/OLDNEWS.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/README.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/TESTING.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/THANKS.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/default.css
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/docutils.conf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/hello.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/pyforttest.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/pytest.py
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/simple.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/simple_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/allocarr.f90
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/allocarr_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/array.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/array_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/calculate.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/calculate_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/callback.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/callback2.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/callback_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/common.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/common_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/compile_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/default.css
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/docutils.conf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/extcallback.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/extcallback_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/fib1.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/fib1.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/fib2.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/fib3.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/ftype.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/ftype_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/index.txt
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/moddata.f90
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/moddata_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/run_main_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/scalar.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/scalar_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/setup_example.py
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/spam.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/spam_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/string.f
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/string_session.dat
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/var.pyf
%doc %{pref}/lib/python2.7/site-packages/numpy/f2py/docs/usersguide/var_session.dat
%{pref}/lib/python2.7/site-packages/numpy/f2py/f2py.1
%{pref}/lib/python2.7/site-packages/numpy/f2py/f2py2e.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/f2py2e.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/f2py_testing.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/f2py_testing.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/f90mod_rules.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/f90mod_rules.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/func2subr.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/func2subr.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/info.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/rules.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/rules.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/setup.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_array_from_pyobj.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_callback.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_mixed.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_return_character.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_return_complex.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_return_integer.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_return_logical.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/test_return_real.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/util.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/use_rules.py
%{pref}/lib/python2.7/site-packages/numpy/f2py/use_rules.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/fft/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/fftpack.py
%{pref}/lib/python2.7/site-packages/numpy/fft/fftpack.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/fftpack_lite.so
%{pref}/lib/python2.7/site-packages/numpy/fft/helper.py
%{pref}/lib/python2.7/site-packages/numpy/fft/helper.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/info.py
%{pref}/lib/python2.7/site-packages/numpy/fft/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/setup.py
%{pref}/lib/python2.7/site-packages/numpy/fft/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/fft/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/fft/tests/test_fftpack.py
%{pref}/lib/python2.7/site-packages/numpy/fft/tests/test_helper.py
%{pref}/lib/python2.7/site-packages/numpy/lib/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/lib/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/_compiled_base.so
%{pref}/lib/python2.7/site-packages/numpy/lib/_datasource.py
%{pref}/lib/python2.7/site-packages/numpy/lib/_datasource.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/_iotools.py
%{pref}/lib/python2.7/site-packages/numpy/lib/_iotools.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/arraysetops.py
%{pref}/lib/python2.7/site-packages/numpy/lib/arraysetops.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/arrayterator.py
%{pref}/lib/python2.7/site-packages/numpy/lib/arrayterator.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/benchmarks/bench_arraysetops.py
%{pref}/lib/python2.7/site-packages/numpy/lib/financial.py
%{pref}/lib/python2.7/site-packages/numpy/lib/financial.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/format.py
%{pref}/lib/python2.7/site-packages/numpy/lib/format.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/function_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/function_base.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/index_tricks.py
%{pref}/lib/python2.7/site-packages/numpy/lib/index_tricks.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/info.py
%{pref}/lib/python2.7/site-packages/numpy/lib/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/npyio.py
%{pref}/lib/python2.7/site-packages/numpy/lib/npyio.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/polynomial.py
%{pref}/lib/python2.7/site-packages/numpy/lib/polynomial.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/recfunctions.py
%{pref}/lib/python2.7/site-packages/numpy/lib/recfunctions.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/scimath.py
%{pref}/lib/python2.7/site-packages/numpy/lib/scimath.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/setup.py
%{pref}/lib/python2.7/site-packages/numpy/lib/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/lib/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/shape_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/shape_base.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/stride_tricks.py
%{pref}/lib/python2.7/site-packages/numpy/lib/stride_tricks.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test__datasource.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test__iotools.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_arraysetops.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_arrayterator.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_financial.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_format.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_function_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_index_tricks.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_io.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_polynomial.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_recfunctions.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_shape_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_stride_tricks.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_twodim_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_type_check.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_ufunclike.py
%{pref}/lib/python2.7/site-packages/numpy/lib/tests/test_utils.py
%{pref}/lib/python2.7/site-packages/numpy/lib/twodim_base.py
%{pref}/lib/python2.7/site-packages/numpy/lib/twodim_base.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/type_check.py
%{pref}/lib/python2.7/site-packages/numpy/lib/type_check.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/ufunclike.py
%{pref}/lib/python2.7/site-packages/numpy/lib/ufunclike.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/user_array.py
%{pref}/lib/python2.7/site-packages/numpy/lib/user_array.pyc
%{pref}/lib/python2.7/site-packages/numpy/lib/utils.py
%{pref}/lib/python2.7/site-packages/numpy/lib/utils.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/info.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/lapack_lite.so
%{pref}/lib/python2.7/site-packages/numpy/linalg/linalg.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/linalg.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/setup.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/linalg/tests/test_build.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/tests/test_linalg.py
%{pref}/lib/python2.7/site-packages/numpy/linalg/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/ma/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/ma/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/bench.py
%{pref}/lib/python2.7/site-packages/numpy/ma/bench.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/core.py
%{pref}/lib/python2.7/site-packages/numpy/ma/core.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/extras.py
%{pref}/lib/python2.7/site-packages/numpy/ma/extras.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/mrecords.py
%{pref}/lib/python2.7/site-packages/numpy/ma/mrecords.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/setup.py
%{pref}/lib/python2.7/site-packages/numpy/ma/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/ma/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_core.py
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_extras.py
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_mrecords.py
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_old_ma.py
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/ma/tests/test_subclassing.py
%{pref}/lib/python2.7/site-packages/numpy/ma/testutils.py
%{pref}/lib/python2.7/site-packages/numpy/ma/testutils.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/timer_comparison.py
%{pref}/lib/python2.7/site-packages/numpy/ma/timer_comparison.pyc
%{pref}/lib/python2.7/site-packages/numpy/ma/version.py
%{pref}/lib/python2.7/site-packages/numpy/ma/version.pyc
%{pref}/lib/python2.7/site-packages/numpy/matlib.py
%{pref}/lib/python2.7/site-packages/numpy/matlib.pyc
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/defmatrix.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/defmatrix.pyc
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/setup.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/tests/test_defmatrix.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/tests/test_multiarray.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/tests/test_numeric.py
%{pref}/lib/python2.7/site-packages/numpy/matrixlib/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/_capi.so
%{pref}/lib/python2.7/site-packages/numpy/numarray/alter_code1.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/alter_code1.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/alter_code2.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/alter_code2.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/compat.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/compat.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/convolve.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/convolve.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/fft.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/fft.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/functions.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/functions.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/image.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/image.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/linear_algebra.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/linear_algebra.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/ma.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/ma.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/matrix.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/matrix.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/mlab.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/mlab.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/nd_image.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/nd_image.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/numerictypes.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/numerictypes.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/random_array.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/random_array.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/session.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/session.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/setup.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/ufuncs.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/ufuncs.pyc
%{pref}/lib/python2.7/site-packages/numpy/numarray/util.py
%{pref}/lib/python2.7/site-packages/numpy/numarray/util.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/alter_code1.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/alter_code1.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/alter_code2.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/alter_code2.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/array_printer.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/array_printer.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/arrayfns.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/arrayfns.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/compat.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/compat.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/fft.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/fft.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/fix_default_axis.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/fix_default_axis.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/functions.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/functions.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/linear_algebra.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/linear_algebra.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/ma.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/ma.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/matrix.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/matrix.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/misc.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/misc.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/mlab.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/mlab.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/precision.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/precision.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/random_array.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/random_array.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/rng.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/rng.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/rng_stats.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/rng_stats.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/setup.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/tests/test_oldnumeric.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/tests/test_regression.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/typeconv.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/typeconv.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/ufuncs.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/ufuncs.pyc
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/user_array.py
%{pref}/lib/python2.7/site-packages/numpy/oldnumeric/user_array.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/chebyshev.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/chebyshev.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polynomial.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polynomial.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polytemplate.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polytemplate.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polyutils.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/polyutils.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/setup.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/polynomial/tests/test_chebyshev.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/tests/test_polynomial.py
%{pref}/lib/python2.7/site-packages/numpy/polynomial/tests/test_polyutils.py
%{pref}/lib/python2.7/site-packages/numpy/random/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/random/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/random/info.py
%{pref}/lib/python2.7/site-packages/numpy/random/info.pyc
%{pref}/lib/python2.7/site-packages/numpy/random/mtrand.so
%{pref}/lib/python2.7/site-packages/numpy/random/setup.py
%{pref}/lib/python2.7/site-packages/numpy/random/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/random/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/random/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/random/tests/test_random.py
%{pref}/lib/python2.7/site-packages/numpy/setup.py
%{pref}/lib/python2.7/site-packages/numpy/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/site.cfg.example
%{pref}/lib/python2.7/site-packages/numpy/testing/__init__.py
%{pref}/lib/python2.7/site-packages/numpy/testing/__init__.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/decorators.py
%{pref}/lib/python2.7/site-packages/numpy/testing/decorators.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/noseclasses.py
%{pref}/lib/python2.7/site-packages/numpy/testing/noseclasses.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/nosetester.py
%{pref}/lib/python2.7/site-packages/numpy/testing/nosetester.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/nulltester.py
%{pref}/lib/python2.7/site-packages/numpy/testing/nulltester.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/numpytest.py
%{pref}/lib/python2.7/site-packages/numpy/testing/numpytest.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/setup.py
%{pref}/lib/python2.7/site-packages/numpy/testing/setup.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/setupscons.py
%{pref}/lib/python2.7/site-packages/numpy/testing/setupscons.pyc
%{pref}/lib/python2.7/site-packages/numpy/testing/tests/test_decorators.py
%{pref}/lib/python2.7/site-packages/numpy/testing/tests/test_utils.py
%{pref}/lib/python2.7/site-packages/numpy/testing/utils.py
%{pref}/lib/python2.7/site-packages/numpy/testing/utils.pyc
%{pref}/lib/python2.7/site-packages/numpy/tests/test_ctypeslib.py
%{pref}/lib/python2.7/site-packages/numpy/tests/test_matlib.py
%{pref}/lib/python2.7/site-packages/numpy/tools/py3tool.py
%{pref}/lib/python2.7/site-packages/numpy/version.py
%{pref}/lib/python2.7/site-packages/numpy/version.pyc
%{pref}/lib/python2.7/site-packages/numpy/core/_dotblas.so

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/numpy/random/randomkit.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/arraybase.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/cfunc.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/ieeespecial.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/libnumarray.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/numcomplex.h
%{pref}/lib/python2.7/site-packages/numpy/numarray/include/numpy/nummacro.h
%{pref}/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.c
%{pref}/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.h
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/src/array_from_pyobj/wrapmodule.c
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo.f
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo_fixed.f90
%{pref}/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo_free.f90
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/src/example.c
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/src/example.i
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/src/zoo.cc
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/src/zoo.h
%{pref}/lib/python2.7/site-packages/numpy/distutils/tests/swig_ext/src/zoo.i
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/__multiarray_api.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/__ufunc_api.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/_numpyconfig.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/arrayobject.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/arrayscalars.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/multiarray_api.txt
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/noprefix.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_3kcompat.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_common.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_cpu.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_endian.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_interrupt.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_math.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/npy_os.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/numpyconfig.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/old_defines.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/oldnumeric.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/ufunc_api.txt
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/ufuncobject.h
%{pref}/lib/python2.7/site-packages/numpy/core/include/numpy/utils.h
%{pref}/lib/python2.7/site-packages/numpy/core/lib/libnpymath.a
