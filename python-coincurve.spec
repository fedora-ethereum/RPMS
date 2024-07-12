Name:          python-coincurve
Version:       20.0.0
Release:       %autorelease
Summary:       Cross-platform Python bindings for libsecp256k1
License:       MIT or ASL-2.0
URL:           https://github.com/ofek/coincurve
Source0:       %{pypi_source coincurve}
Patch1:        python-coincurve-0001-Re-add-tests-forgotten-in-PyPi.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: python3-asn1crypto
BuildRequires: python3-cffi
BuildRequires: python3-codecov
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-tox-current-env
BuildRequires: python3-wheel
BuildRequires: tox
Provides: bundled(libsecp256k1)
%{?python_provide:%python_provide python3-coincurve}

%description
Cross-platform Python bindings for libsecp256k1.

%prep
%autosetup -p1 -n coincurve-%{version}

%build
%py3_build

%install
%py3_install

%check
%tox

%files
%license LICENSE-MIT LICENSE-APACHE
#%%doc docs
%doc README.md
%{python3_sitearch}/coincurve/
%{python3_sitearch}/coincurve-*.egg-info/

%changelog
%autochangelog
