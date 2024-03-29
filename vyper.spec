Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.3.10
Release:	%autorelease
BuildArch:	noarch
License:	ASL 2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source vyper}
Patch1:		vyper-0001-Use-Cryptodomex.patch
Patch2:		vyper-0002-Ease-version-requirements.patch
BuildRequires:	git
BuildRequires:	python-base58
BuildRequires:	python-eth_tester
BuildRequires:	python-multiaddr
BuildRequires:	python-web3
BuildRequires:	python3-asttokens
BuildRequires:	python3-cached_property
BuildRequires:	python3-importlib-metadata
BuildRequires:	python3-pip
BuildRequires:	python3-pycryptodomex
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-rpm-generators
BuildRequires:	python3-rpm-macros
BuildRequires:	python3-semantic_version
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	python3-wheel
BuildRequires:	sed
%{?python_provide:%python_provide python3-vyper}


%description
Pythonic Smart Contract Language for the EVM.

%prep
%autosetup -p1
# v0.3.10 == 9136169468f317a53b4e7448389aa315f90b95ba
echo "91361694" > "./vyper_git_commithash.txt"


%build
%py3_build

%install
%py3_install
rm -f %{buildroot}/usr/vyper_git_commithash.txt
rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
# FIXME not enough dependencies
#%%pytest

%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/fang
%{_bindir}/vyper
%{_bindir}/vyper-json
%{_bindir}/vyper-serve
%{python3_sitelib}/vyper/
%{python3_sitelib}/vyper-*.egg-info/

%changelog
%autochangelog
