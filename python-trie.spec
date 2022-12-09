Name:          python-trie
Version:       2.0.2
Release:       %autorelease
BuildArch:     noarch
Summary:       Library which implements the Ethereum Trie structure
License:       MIT
URL:           https://github.com/ethereum/py-trie
Source0:       %{pypi_source trie}
BuildRequires: python-eth_hash
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python-rlp
BuildRequires: python3-hypothesis
BuildRequires: python3-pycryptodomex
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sortedcontainers
BuildRequires: sed
%{?python_provide:%python_provide python3-trie}

%description
Self-describing content-addressed identifiers for distributed systems
implementation in Python.

%prep
%autosetup -p1 -n trie-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc CHANGELOG README.md
%{python3_sitelib}/trie/
%{python3_sitelib}/trie-*.egg-info/

%changelog
%autochangelog
