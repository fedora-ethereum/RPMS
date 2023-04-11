Summary:       A framework for smart contracts for EVM
Name:          brownie
Version:       1.19.2
Release:       %autorelease
BuildArch:     noarch
License:       ASL 2.0
URL:           https://github.com/eth-brownie/brownie
Source0:       %{pypi_source eth-brownie}
Patch1:        brownie-0001-Adjust-versions.patch
BuildRequires: python-eip712
BuildRequires: python-eth_abi
BuildRequires: python-eth_account
BuildRequires: python-eth_hash
BuildRequires: python-eth_keyfile
BuildRequires: python-eth_rlp
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python3-setuptools
BuildRequires: python3-aiohttp
BuildRequires: python3-asttokens
BuildRequires: python3-black
BuildRequires: python3-certifi
BuildRequires: python3-charset-normalizer
BuildRequires: python3-cytoolz
BuildRequires: python3-pycryptodomex
BuildRequires: python3-semantic_version
BuildRequires: python3-hypothesis
BuildRequires: python3-idna
#BuildRequires: python3-cached_property
#BuildRequires: python3-importlib-metadata
#BuildRequires: python3-wheel
#BuildRequires: sed
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-brownie}
Requires: python-base58
Requires: python-lazy_load
Requires: python-multiaddr
Requires: python-trie


%description
A Python-based development and testing framework for smart contracts targeting
the Ethereum Virtual Machine.


%prep
%autosetup -p1 -n eth-brownie-%{version}
# FIXME we do not rely on pre-generated requirements.txt
cp -arv requirements.in requirements.txt
sed -i -e "	s,pycryptodome>=3.5.1\,<4,pycryptodomex>=3.5.1,g;
		s,semantic-version>=2.10\,<3,semantic-version>=2.8\,<3,g;
		s,asttokens==2.0.5,asttokens>=2.0.5,g" setup.py

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
%license LICENSE
%doc README.md
%{_bindir}/brownie
%{python3_sitelib}/brownie/
%{python3_sitelib}/eth_brownie-*.egg-info/

%changelog
%autochangelog
