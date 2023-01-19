Name:          python-web3
Version:       5.31.3
Release:       %autorelease
BuildArch:     noarch
Summary:       A library for interacting with the Ethereum blockchain and ecosystem
License:       MPL 2.0
URL:           https://github.com/ethereum/web3.py
Source0:       %{pypi_source web3}
BuildRequires: python-eth_abi
BuildRequires: python-eth_account
BuildRequires: python-eth_hash
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python-ipfshttpclient
BuildRequires: python-lru-dict
BuildRequires: python3-aiohttp
BuildRequires: python3-jsonschema
BuildRequires: python3-protobuf
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-websockets
BuildRequires: sed
%{?python_provide:%python_provide python3-web3}

%description
A library for interacting with the Ethereum blockchain and ecosystem.

%prep
%autosetup -p1 -n web3-%{version}
sed -i -e "	s,eth-abi>=2.2.0\,<3.0.0,eth-abi>=2.2.0,g;
		s,eth-account>=0.5.9\,<0.6.0,eth-account>=0.5.9,g;
		s,eth-hash\[pycryptodome\]>=0.2.0\,<1.0.0,eth-hash>=0.2.0,g;
		s,eth-rlp<0.3,eth-rlp<=0.3,g;
		s,eth-typing>=2.0.0\,<3.0.0,eth-typing>=2.0.0,g;
		s,eth-utils>=1.9.5\,<2.0.0,eth-utils>=1.9.5,g;
		s,protobuf==3.19.5,protobuf>=3.19.4,g;
		s,websockets>=9.1\,<10,websockets>=9.1,g" setup.py

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/ens/
%{python3_sitelib}/ethpm/
%{python3_sitelib}/web3/
%{python3_sitelib}/web3-*.egg-info/

%changelog
%autochangelog
