Name:          python-eth_keys
Version:       0.5.0
Release:       %autorelease
BuildArch:     noarch
Summary:       A common API for Ethereum key operations.
License:       MIT
URL:           https://github.com/ethereum/eth-keys
Source0:       %{pypi_source eth-keys}
Patch1:        python-eth_keys-0001-Remove-asn1tools-as-a-dependency.patch
BuildRequires: python-coincurve
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python3-factory-boy
BuildRequires: python3-hypothesis
BuildRequires: python3-pyasn1
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_keys}

%description
RLP definitions for common Ethereum objects in Python.

%prep
%autosetup -p1 -n eth-keys-%{version}

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
