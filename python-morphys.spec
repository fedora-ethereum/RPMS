%global git_tag 0642a71126c32cd26b3a443a5cac27e4e1f7240f

Name:          python-morphys
Version:       1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Smart conversions between unicode and bytes types
License:       MPL 2.0
URL:           https://github.com/mkalinski/morphys
Source0:       https://github.com/mkalinski/morphys/archive/%{git_tag}/morphys-1.0.tar.gz
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-morphys}

%description
Smart conversions between unicode and bytes types for common cases in python.

%prep
%autosetup -p1 -n morphys-%{git_tag}

%build
%py3_build

%install
%py3_install

%check
%python3 ./tests.py
#%%pytest

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/morphys.py
%{python3_sitelib}/morphys-*.egg-info/

%changelog
%autochangelog
