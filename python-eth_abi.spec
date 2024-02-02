Name:          python-eth_abi
Version:       5.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python utilities for working with Ethereum ABI definitions
License:       MIT
URL:           https://github.com/ethereum/eth-abi
Source0:       %{pypi_source eth_abi}
#Patch1:        python-eth_abi-0001-Don-t-use-reserved-words.patch
BuildRequires: python-eth_hash
BuildRequires: python-eth_typing
BuildRequires: python-eth_utils
BuildRequires: python-compat-parsimonious09
BuildRequires: python3-hypothesis
BuildRequires: python3-jinja2
BuildRequires: python3-pytest
#BuildRequires: python3-pytest-pythonpath
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-towncrier
BuildRequires: sed
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_abi}

%description
eth_abi: Python utilities for working with Ethereum ABI definitions, especially
encoding and decoding.

%prep
%autosetup -p1 -n eth_abi-%{version}
#sed -i -e "s,\,<0.9.0,,g" setup.py

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
%{python3_sitelib}/eth_abi/
%{python3_sitelib}/eth_abi-*.egg-info/

%changelog
%autochangelog
