Name:          python-solcast
Version:       0.2.1
Release:       %autorelease
BuildArch:     noarch
Summary:       A Python client library for the Solcast API
License:       MIT
URL:           https://github.com/cjtapper/solcast-py
Source0:       %{pypi_source solcast}
BuildRequires: python3-isodate
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-solcast}

%description
A Python client library for the Solcast API.

%prep
%autosetup -p1 -n solcast-%{version}

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
#%%license LICENSE.md
%doc README.rst
%{python3_sitelib}/solcast/
%{python3_sitelib}/solcast-*.egg-info/

%changelog
%autochangelog
