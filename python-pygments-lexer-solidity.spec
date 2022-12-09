Name:          python-pygments-lexer-solidity
Version:       0.7.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Solidity lexer for Pygments
License:       BSD
URL:           https://gitlab.com/veox/pygments-lexer-solidity
Source0:       %{pypi_source pygments-lexer-solidity}
BuildRequires: python3-pygments
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-pygments-lexer-solidity}

%description
Solidity lexer for Pygments.

%prep
%autosetup -p1 -n pygments-lexer-solidity-%{version}

%build
%py3_build

%install
%py3_install

%check
# FIXME
# pip install -r requirements.txt
# pip install -e .
# pygmentize example.sol
# pygmentize example.yul

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pygments_lexer_solidity/
%{python3_sitelib}/pygments_lexer_solidity-*.egg-info

%changelog
%autochangelog
