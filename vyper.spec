Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.3.7
Release:	%autorelease
BuildArch:	noarch
License:	ASL 2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source vyper}
Patch1:		vyper-0001-Use-Cryptodome.patch
BuildRequires:	python3-asttokens
BuildRequires:	python3-cached_property
BuildRequires:	python3-importlib-metadata
BuildRequires:	python3-pycryptodomex
BuildRequires:	python3-rpm-macros
BuildRequires:	python3-semantic_version
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	sed
%{?python_provide:%python_provide python3-vyper}


%description
Pythonic Smart Contract Language for the EVM.

%prep
%autosetup -p1
sed -i -e "	s,pycryptodome>=3.5.1\,<4,pycryptodomex>=3.5.1,g;
		s,semantic-version>=2.10\,<3,semantic-version>=2.8\,<3,g;
		s,asttokens==2.0.5,asttokens>=2.0.5,g" setup.py

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}/usr/vyper_git_commithash.txt

%check
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
# FIXME
%{python3_sitelib}/tests/

%changelog
%autochangelog
