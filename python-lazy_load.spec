Name:          python-lazy_load
Version:       0.8.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A minimalistic interface that allows lazy evaluation
License:       MIT
URL:           https://github.com/kutoga/lazy-load
Source0:       %{pypi_source lazy_load}
BuildRequires: python3-lazy-object-proxy
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-cid}

%description
A minimalistic interface that allows lazy evaluation of expressions and
function calls.

%prep
%autosetup -p1 -n lazy-load-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/lazy_load/
%{python3_sitelib}/lazy_load-*.egg-info/

%changelog
%autochangelog
