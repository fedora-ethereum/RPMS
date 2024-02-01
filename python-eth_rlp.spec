Name:          python-eth_rlp
Version:       1.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       RLP definitions for common Ethereum objects in Python
License:       MIT
URL:           https://github.com/ethereum/eth-rlp
Source0:       %{pypi_source eth-rlp}
BuildRequires: python-eth_hash
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python-rlp
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-towncrier
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_rlp}

%description
RLP definitions for common Ethereum objects in Python.

%prep
%autosetup -p1 -n eth-rlp-%{version}
#sed -i -e "s,<0.9.0,<0.10.0,g" setup.py

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
%{python3_sitelib}/eth_rlp/
%{python3_sitelib}/eth_rlp-*.egg-info/

%changelog
%autochangelog
