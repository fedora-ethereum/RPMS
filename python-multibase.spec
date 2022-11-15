Name:          python-multibase
Version:       1.0.3
Release:       %autorelease
BuildArch:     noarch
Summary:       Multibase implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-multibase
Source0:       %{pypi_source py-multibase}
Patch1:        python-multibase-0001-Fix-issues-with-py.test.patch
BuildRequires: python-baseconv
BuildRequires: python-morphys
BuildRequires: python3-pip
BuildRequires: python3-pytest
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-wheel
%{?python_provide:%python_provide python3-multibase}

%description
Multibase implementation in Python.

%prep
%autosetup -p1 -n py-multibase-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/multibase/
%{python3_sitelib}/py_multibase-*.egg-info/

%changelog
%autochangelog
