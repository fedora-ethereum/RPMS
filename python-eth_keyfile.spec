Name:          python-eth_keyfile
Version:       0.6.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for handling the encrypted keyfile format used to store private keys
License:       MIT
URL:           https://github.com/ethereum/eth-keyfile
Source0:       %{pypi_source eth-keyfile}
Patch1:        python-eth_keyfile-0001-remove-deprecated-setuptools-markdown-bump-setuptool.patch
Patch2:        python-eth_keyfile-0002-Fedora-use-cryptodome-explicitly.patch
BuildRequires: python-eth_keys
BuildRequires: python-eth_utils
BuildRequires: python3-pycryptodomex
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_keyfile}

%description
Tools for handling the encrypted keyfile format used to store private keys.

%prep
%autosetup -p1 -n eth-keyfile-%{version}
sed -i -e "s,0.4.0\,<0.5.0,0.3.4,g;s,pycryptodome,pycryptodomex,g" setup.py

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
%{python3_sitelib}/eth_keyfile/
%{python3_sitelib}/eth_keyfile-*.egg-info/

%changelog
%autochangelog
