#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ansible_builder
Version  : 1.1.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/3b/95/9f21cc9066b63dde666a662d2d8d20ff43005c25facb13885651c6c2d346/ansible-builder-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/95/9f21cc9066b63dde666a662d2d8d20ff43005c25facb13885651c6c2d346/ansible-builder-1.1.0.tar.gz
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
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
%setup -q -n ansible-builder-1.1.0
cd %{_builddir}/ansible-builder-1.1.0
pushd ..
cp -a ansible-builder-1.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666311987
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ansible_builder
cp %{_builddir}/ansible-builder-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-ansible_builder/1d64793d909db14ba52ed909fefa9f8cec85720d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
