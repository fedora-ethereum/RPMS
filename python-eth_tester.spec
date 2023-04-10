Name:          python-eth_tester
Version:       0.8.0
Release:       0.b3.%autorelease
BuildArch:     noarch
Summary:       Tool suite for testing ethereum applications
License:       MIT
URL:           https://github.com/ethereum/eth-tester
# FIXME no tests shipped to pypi. Should we just grab tarball from github?
# See comments below
#Source0:       %{pypi_source eth-tester}
Source0:        https://github.com/ethereum/eth-tester/archive/v0.8.0-beta.3/eth_tester-%{version}.tar.gz
BuildRequires: python-eth_abi
BuildRequires: python-eth_account
BuildRequires: python-eth_hash
BuildRequires: python-eth_keys
BuildRequires: python-eth_utils
BuildRequires: python-rlp
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-semantic_version
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_tester}

%description
Tool suite for testing ethereum applications.

%prep
%autosetup -p1 -n eth-tester-%{version}-beta.3
sed -i -e "s,eth-hash\[pycryptodome\],eth-hash,g" setup.py
# FIXME return as soon as we package py-evm
rm -rf tests/backends

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
%doc README.md
%{python3_sitelib}/eth_tester/
%{python3_sitelib}/eth_tester-*.egg-info/

%changelog
%autochangelog
