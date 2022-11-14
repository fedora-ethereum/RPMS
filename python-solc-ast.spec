Name:          python-solc-ast
Version:       1.2.9
Release:       %autorelease
BuildArch:     noarch
Summary:       A tool for exploring the solc abstract syntax tree
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/py-solc-ast
Source0:       %{pypi_source py-solc-ast}
BuildRequires: python-solcast
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-solc-ast}

%description
A tool for exploring the solc abstract syntax tree.

%prep
%autosetup -p1 -n py-solc-ast-%{version}

%build
%py3_build

%install
%py3_install


%check
#%%pytest tests/

%files
#%%license LICENSE
#%%doc docs
%doc README.md
# FIXME conflicts with python-solcast
%{python3_sitelib}/solcast/*
%{python3_sitelib}/py_solc_ast-*.egg-info/

%changelog
%autochangelog
