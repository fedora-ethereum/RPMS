Name:          python-coincurve
Version:       17.0.0
Release:       %autorelease
Summary:       Cross-platform Python bindings for libsecp256k1
License:       MIT or ASL-2.0
URL:           https://github.com/ofek/coincurve
Source0:       %{pypi_source coincurve}
BuildRequires: gcc
BuildRequires: libsecp256k1-devel
BuildRequires: python3-asn1crypto
BuildRequires: python3-cffi
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: tox
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
#%%pytest
tox

%files
#%%license LICENSE-MIT LICENSE-APACHE
#%%doc docs
%doc README.md
%{python3_sitearch}/coincurve/
%{python3_sitearch}/coincurve-*.egg-info/

%changelog
%autochangelog
