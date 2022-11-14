Name:          python-eth_event
Version:       1.2.3
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for Ethereum event decoding and topic generation.
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/eth-event
Source0:       %{pypi_source eth-event}
BuildRequires: python-eth_abi
BuildRequires: python-eth_hash
BuildRequires: python-eth_utils
BuildRequires: python-hexbytes
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: sed
%{?python_provide:%python_provide python3-eth_event}

%description
Tools for Ethereum event decoding and topic generation.

%prep
%autosetup -p1 -n eth-event-%{version}
sed -i -e "s,eth-abi>=2.0.0\,<3.0.0,eth-abi>=2.0.0,g;
	s,eth-hash\[pycryptodome\],eth-hash,g;
	s,eth-utils>=1.2.0\,<2.0.0,eth-utils>=1.2.0,g" setup.py

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
#%%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/eth_event/
%{python3_sitelib}/eth_event-*.egg-info/

%changelog
%autochangelog
