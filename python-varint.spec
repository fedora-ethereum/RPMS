Name:          python-varint
Version:       1.0.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic varint implementation in python
License:       MIT
URL:           https://github.com/fmoo/python-varint
Source0:       %{pypi_source varint}
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-varint}

%description
A basic varint implementation in python.

%prep
%autosetup -p1 -n varint-%{version}

%build
%py3_build

%install
%py3_install

%files
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/varint-*.egg-info/
%{python3_sitelib}/varint.py

%changelog
%autochangelog
