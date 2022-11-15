Name:          python-baseconv
Version:       1.2.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic baseconv implementation in python
License:       PSF-2.0
URL:           https://github.com/semente/python-baseconv
Source0:       %{pypi_source python-baseconv}
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-baseconv}

%description
A basic baseconv implementation in python.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
# FIXME - no tests

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/python_baseconv-*.egg-info/
%{python3_sitelib}/baseconv.py

%changelog
%autochangelog
