Name:          python-eth_keys
Version:       0.3.4
Release:       %autorelease
BuildArch:     noarch
Summary:       A common API for Ethereum key operations.
License:       MIT
URL:           https://github.com/ethereum/eth-keys
Source0:       %{pypi_source eth-keys}
BuildRequires: python-coincurve
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_keys}

%description
RLP definitions for common Ethereum objects in Python.

%prep
%autosetup -p1 -n eth-keys-%{version}
sed -i -e "s,\,<2.0.0,,g;s,\,<3.0.0,,g;s,\,<13.0.0,,g" setup.py

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
%{python3_sitelib}/eth_keys/
%{python3_sitelib}/eth_keys-*.egg-info/

%changelog
%autochangelog
