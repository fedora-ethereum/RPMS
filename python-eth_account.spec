Name:          python-eth_account
Version:       0.12.3
Release:       %autorelease
BuildArch:     noarch
Summary:       Account abstraction library for web3.py
License:       MIT
URL:           https://github.com/ethereum/eth-account
Source0:       %{pypi_source eth-account}
BuildRequires: python-bitarray
BuildRequires: python-eth_abi
BuildRequires: python-eth_keyfile
BuildRequires: python-eth_keys
BuildRequires: python-eth_rlp
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python-rlp
BuildRequires: python3-coverage
BuildRequires: python3-hypothesis
BuildRequires: python3-jinja2
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-towncrier
BuildRequires: sed
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_account}

%description
Account abstraction library for web3.py.

%prep
%autosetup -p1 -n eth-account-%{version}
sed -i -e "s,0.4.0\,<0.5,0.3.4,g" setup.py

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
%{python3_sitelib}/eth_account/
%{python3_sitelib}/eth_account-*.egg-info/

%changelog
%autochangelog
