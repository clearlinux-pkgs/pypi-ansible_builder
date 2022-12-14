#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ansible_builder
Version  : 1.2.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/45/ed/6ce94d6b28789d8c21cd4d0ba92899688164e883b1bd5660d4e40a974fea/ansible-builder-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/ed/6ce94d6b28789d8c21cd4d0ba92899688164e883b1bd5660d4e40a974fea/ansible-builder-1.2.0.tar.gz
Summary  : "A tool for building Ansible Execution Environments"
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-ansible_builder-bin = %{version}-%{release}
Requires: pypi-ansible_builder-license = %{version}-%{release}
Requires: pypi-ansible_builder-python = %{version}-%{release}
Requires: pypi-ansible_builder-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bindep)
BuildRequires : pypi(pbr)
BuildRequires : pypi(py)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requirements_parser)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![CI](https://github.com/ansible/ansible-builder/actions/workflows/ci.yml/badge.svg?branch=devel)](https://github.com/ansible/ansible-builder/actions?query=branch%3Adevel)
[![codecov](https://codecov.io/gh/ansible/ansible-builder/branch/devel/graph/badge.svg?token=4F6P3DBI40)](https://codecov.io/gh/ansible/ansible-builder)

%package bin
Summary: bin components for the pypi-ansible_builder package.
Group: Binaries
Requires: pypi-ansible_builder-license = %{version}-%{release}

%description bin
bin components for the pypi-ansible_builder package.


%package license
Summary: license components for the pypi-ansible_builder package.
Group: Default

%description license
license components for the pypi-ansible_builder package.


%package python
Summary: python components for the pypi-ansible_builder package.
Group: Default
Requires: pypi-ansible_builder-python3 = %{version}-%{release}

%description python
python components for the pypi-ansible_builder package.


%package python3
Summary: python3 components for the pypi-ansible_builder package.
Group: Default
Requires: python3-core
Provides: pypi(ansible_builder)
Requires: pypi(bindep)
Requires: pypi(pyyaml)
Requires: pypi(requirements_parser)

%description python3
python3 components for the pypi-ansible_builder package.


%prep
%setup -q -n ansible-builder-1.2.0
cd %{_builddir}/ansible-builder-1.2.0
pushd ..
cp -a ansible-builder-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672254421
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ansible_builder
cp %{_builddir}/ansible-builder-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-ansible_builder/1d64793d909db14ba52ed909fefa9f8cec85720d
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

%files bin
%defattr(-,root,root,-)
/usr/bin/ansible-builder

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ansible_builder/1d64793d909db14ba52ed909fefa9f8cec85720d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
