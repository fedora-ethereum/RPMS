Name:          python-thx
Version:       1.7.3
Release:       %autorelease
BuildArch:     noarch
Summary:       A Python library for the MythX platform
License:       MIT
URL:           https://github.com/ConsenSys/pythx
Source0:       %{pypi_source pythx}
Patch1:        python-thx-0001-Upgrade-PyJWT-1.7.1-2.4.0.patch
BuildRequires: python-mythx-models
BuildRequires: python3-dateutil
BuildRequires: python3-inflection
BuildRequires: python3-jwt
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-runner
BuildRequires: python3-requests
BuildRequires: python3-requests-mock
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-thx}

%description
A Python library for the MythX platform.

%prep
%autosetup -p1 -n pythx-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
# FIXME rebuild docs
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/pythx-*.egg-info/
%{python3_sitelib}/pythx/

%changelog
%autochangelog
