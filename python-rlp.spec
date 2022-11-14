Name:          python-rlp
Version:       3.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       The python RLP serialization library
License:       MIT
URL:           https://github.com/ilanschnell/rlp
Source0:       %{pypi_source rlp}
Patch1:        python-rlp-0001-Switch-to-built-in-setuptools-functionality.patch
BuildRequires: python-eth_utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: tox
%{?python_provide:%python_provide python3-rlp}

%description
A Python implementation of Recursive Length Prefix encoding (RLP).

%prep
%autosetup -p1 -n rlp-%{version}

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
%{python3_sitelib}/rlp/
%{python3_sitelib}/rlp-*.egg-info/

%changelog
%autochangelog
