Summary:	A framework for smart contracts for EVM
Name:		brownie
Version:	1.19.2
Release:        %autorelease
BuildArch:	noarch
License:	ASL 2.0
URL:		https://github.com/eth-brownie/brownie
Source0:        %{pypi_source eth-brownie}
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
%{?python_provide:%python_provide python3-brownie}



%description
A Python-based development and testing framework for smart contracts targeting
the Ethereum Virtual Machine.

  - не содержится ничего из python3.11dist(eth-hash[pycryptodome]) = 0.3.3 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(hexbytes) = 0.2.3 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(hypothesis) = 6.27.3 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(idna) = 3.4 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(inflection) = 0.5 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(jsonschema) = 3.2 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(mythx-models) = 1.9.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(parsimonious) = 0.8.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(prompt-toolkit) = 3.0.31 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(protobuf) = 3.19.5 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(psutil) = 5.9.2 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pygments) = 2.13 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pyjwt) = 1.7.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pytest) = 6.2.5 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pytest-xdist) = 1.34 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(python-dateutil) = 2.8.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(python-dotenv) = 0.16 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pythx) = 1.6.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(pyyaml) = 5.4.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(rlp) = 2.0.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(toolz) = 0.12 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(websockets) = 9.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(wrapt) = 1.14.1 необходимого для brownie-1.19.2-1.fc37.noarch
  - не содержится ничего из python3.11dist(yarl) = 1.8.1 необходимого для brownie-1.19.2-1.fc37.noarch

bumpversion
coverage
flake8==3.9.1
isort
mypy==0.720
pip-tools
pytest-cov
pytest-mock
sphinx
sphinx_rtd_theme
tox
twine
wheel

black>=20.8b1
eip712<=0.1.0
eth-abi<3
eth-account<0.6.0
eth-event>=1.2.1,<2
eth-hash[pycryptodome]<1
eth-rlp<0.3.0
eth-utils<2
hexbytes<1
hypothesis<6.28.0
lazy-object-proxy>=1.6.0,<2
prompt-toolkit<4
psutil>=5.7.3,<6
py-solc-ast>=1.2.8,<2
py-solc-x>=1.1.0,<2
py>=1.5.0,<2
pygments-lexer-solidity<1
pygments<3
pytest-xdist<2
pytest<7
python-dotenv>=0.16.0,<0.17.0
pythx<=1.6.1
pyyaml>=5.3.0,<6
requests>=2.25.0,<3
rlp<3
semantic-version<3
tqdm<5
vvm>=0.1.0,<1
vyper>=0.2.11,<1
web3>=5.22.0,<6
wrapt>=1.12.1,<2

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
