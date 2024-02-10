Name:          python-eth_typing
Version:       4.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python types for type hinting commonly used ethereum types
License:       MIT
URL:           https://github.com/ethereum/eth-typing
Source0:       %{pypi_source eth-typing}
BuildRequires: python3-jinja2
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-towncrier
BuildRequires: tox
%{?python_provide:%python_provide python3-eth_typing}

%description
Python types for type hinting commonly used ethereum types.

%prep
%autosetup -p1 -n eth-typing-%{version}

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
%{python3_sitelib}/eth_typing/
%{python3_sitelib}/eth_typing-*.egg-info/

%changelog
%autochangelog
