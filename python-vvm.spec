Name:          python-vvm
Version:       0.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Vyper version manager
License:       MIT
URL:           https://github.com/vyperlang/vvm
Source0:       %{pypi_source vvm}
Patch1:        python3-vvm-0001-Switch-to-built-in-setuptols-functionality.patch
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
%{?python_provide:%python_provide python3-vvm}

%description
Vyper version manager.

%prep
%autosetup -p1 -n vvm-%{version}

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
%{python3_sitelib}/vvm/
%{python3_sitelib}/vvm-*.egg-info/

%changelog
%autochangelog
