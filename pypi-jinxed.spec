#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jinxed
Version  : 1.2.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/a5/3f/5b9182af8108c6af21183fa64883a1c7647450b6d4fa8ad359d4e93f6bd9/jinxed-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/3f/5b9182af8108c6af21183fa64883a1c7647450b6d4fa8ad359d4e93f6bd9/jinxed-1.2.0.tar.gz
Summary  : Jinxed Terminal Library
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: pypi-jinxed-license = %{version}-%{release}
Requires: pypi-jinxed-python = %{version}-%{release}
Requires: pypi-jinxed-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. start-badges
| |docs| |appveyor| |travis| |codecov|
| |pypi| |supported-versions| |supported-implementations|
| |linux| |windows| |mac| |bsd|

%package license
Summary: license components for the pypi-jinxed package.
Group: Default

%description license
license components for the pypi-jinxed package.


%package python
Summary: python components for the pypi-jinxed package.
Group: Default
Requires: pypi-jinxed-python3 = %{version}-%{release}

%description python
python components for the pypi-jinxed package.


%package python3
Summary: python3 components for the pypi-jinxed package.
Group: Default
Requires: python3-core
Provides: pypi(jinxed)

%description python3
python3 components for the pypi-jinxed package.


%prep
%setup -q -n jinxed-1.2.0
cd %{_builddir}/jinxed-1.2.0
pushd ..
cp -a jinxed-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398019
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jinxed
cp %{_builddir}/jinxed-1.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jinxed/d22157abc0fc0b4ae96380c09528e23cf77290a9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jinxed/d22157abc0fc0b4ae96380c09528e23cf77290a9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
