Name:          python-solcx
Version:       2.0.2
Release:       %autorelease
BuildArch:     noarch
Summary:       Python wrapper and version management tool for the solc Solidity compiler
License:       MIT
URL:           https://github.com/ApeWorX/py-solc-x
Source0:       %{pypi_source py-solc-x}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-mock
BuildRequires: python3-pytest-xdist
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-wheel
BuildRequires: sed
BuildRequires: twine
%{?python_provide:%python_provide python3-solcx}

%description
Python wrapper and version management tool for the solc Solidity compiler.

%prep
%autosetup -p1 -n py-solc-x-%{version}

%build
%py3_build

%install
%py3_install

%check
# FIXME - no Tox config available
# tox

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/solcx/
%{python3_sitelib}/py_solc_x-*.egg-info/

%changelog
%autochangelog
