Name:          python-eth_utils
Version:       3.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Utility functions for working with ethereum related codebases
License:       MIT
URL:           https://github.com/ethereum/eth-utils
Source0:       %{pypi_source eth-utils}
BuildRequires: python-eth_hash
BuildRequires: python-eth_typing
BuildRequires: python3-cached_property
BuildRequires: python3-cytoolz
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-toolz
BuildRequires: python3-towncrier
BuildRequires: sed
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_utils}

%description
Utility functions for working with ethereum related codebases.

%prep
%autosetup -p1 -n eth-utils-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest ./tests

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/eth_utils/
%{python3_sitelib}/eth_utils-*.egg-info/

%changelog
%autochangelog
