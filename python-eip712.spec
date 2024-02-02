Name:          python-eip712
Version:       0.2.4
Release:       %autorelease
BuildArch:     noarch
Summary:       Message classes for typed structured data hashing and signing in Ethereum
License:       ASL-2.0
URL:           https://github.com/ApeWorX/eip712
Source0:       %{pypi_source eip712}
BuildRequires: python-dataclassy
BuildRequires: python-eth_abi
BuildRequires: python-eth_account
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python3-hypothesis
BuildRequires: python3-myst-parser
BuildRequires: python3-pip
BuildRequires: python3-pycryptodomex
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-click
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-wheel
BuildRequires: sed
%{?python_provide:%python_provide python3-eip712}

%description
Message classes for typed structured data hashing and signing in Ethereum.

%prep
%autosetup -p1 -n eip712-%{version}
sed -i -e "s,eth-hash\[pycryptodome\],eth-hash,g;s,dataclassy>=0.8.2\,<1,dataclassy>=0.8.2,g" setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/eip712/
%{python3_sitelib}/eip712-*.egg-info/

%changelog
%autochangelog
