Name:          python-eth_hash
Version:       0.5.1
Release:       %autorelease
BuildArch:     noarch
Summary:       The Ethereum hashing function
License:       MIT
URL:           https://github.com/ethereum/eth-hash
Source0:       %{pypi_source eth-hash}
Patch1:        python-eth_hash-0001-Fedora-use-cryptodome-explicitly.patch
BuildRequires: python-pycryptodomex
BuildRequires: python3-jinja2
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-towncrier
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_hash}

%description
The Ethereum hashing function, keccak256, sometimes (erroneously) called sha256 or sha3.

%prep
%autosetup -p1 -n eth-hash-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest ./tests/core/ ./tests/backends/pycryptodome

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/eth_hash/
%{python3_sitelib}/eth_hash-*.egg-info/

%changelog
%autochangelog
