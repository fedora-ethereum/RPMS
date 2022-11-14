Name:          python-solcx
Version:       1.1.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Python wrapper and version management tool for the solc Solidity compiler
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/py-solc-x
Source0:       %{pypi_source py-solc-x}
Patch1:        python-solcx-0001-Switch-to-built-in-setuptols-functionality.patch
BuildRequires: black
BuildRequires: bumpversion
BuildRequires: python3-flake8
BuildRequires: python3-isort
BuildRequires: python3-mypy
#BuildRequires: python3-pypandoc
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-mock
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-semantic_version
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-tqdm
BuildRequires: python3-wheel
BuildRequires: sed
BuildRequires: tox
BuildRequires: twine
%{?python_provide:%python_provide python3-solcx}

%description
Python wrapper and version management tool for the solc Solidity compiler.

%prep
%autosetup -p1 -n py-solc-x-%{version}

%build
%py3_build

%install
%py3_install

%check
#%%pytest tests/

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/solcx/
%{python3_sitelib}/py_solc_x-*.egg-info/

%changelog
%autochangelog
