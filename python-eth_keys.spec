Name:          python-eth_keys
Version:       0.3.4
Release:       %autorelease
BuildArch:     noarch
Summary:       A common API for Ethereum key operations.
License:       MIT
URL:           https://github.com/ethereum/eth-keys
# FIXME no tests shipped to pypi. Should we just grab tarball from github?
# See comments below
#Source0:       %{pypi_source eth-keys}
# FIXME they messed up with tags
#Source:        https://github.com/ethereum/eth-keys/archive/v%{version}/eth_keys-%{version}.tar.gz
Source:        https://github.com/ethereum/eth-keys/archive/1b52a4d6ad23f7d8819739a58426baf1c067d9e0/eth_keys-%{version}.tar.gz
BuildRequires: python-coincurve
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_keys}

%description
RLP definitions for common Ethereum objects in Python.

%prep
# FIXME they messed up with tags
#%%autosetup -p1 -n eth-keys-%{version}
%autosetup -p1 -n eth-keys-1b52a4d6ad23f7d8819739a58426baf1c067d9e0
sed -i -e "s,\,<2.0.0,,g;s,\,<3.0.0,,g;s,\,<13.0.0,,g" setup.py

%build
%py3_build

%install
%py3_install

%check
# FIXME no tests shipped to pypi. Should we just grab tarball from github?
# See comments above
%pytest

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/eth_keys/
%{python3_sitelib}/eth_keys-*.egg-info/

%changelog
%autochangelog
