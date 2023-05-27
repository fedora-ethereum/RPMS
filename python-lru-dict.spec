Name:          python-lru-dict
Version:       1.2.0
Release:       %autorelease
Summary:       A fast and memory efficient LRU cache
License:       MIT
URL:           https://github.com/amitdev/lru-dict
Source0:       %{pypi_source lru-dict}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-lru-dict}

%description
A fast and memory efficient LRU cache.

%prep
%autosetup -p1 -n lru-dict-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog
%autochangelog
