Name:          python-mythx-models
Version:       2.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python domain model classes for the MythX platform
License:       MIT
URL:           https://github.com/ConsenSys/mythx-models
Source0:       %{pypi_source mythx-models}
BuildRequires: python3-dateutil
BuildRequires: python3-hypothesis
BuildRequires: python3-inflection
BuildRequires: python3-jsonschema
BuildRequires: python3-pydantic
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-mythx-models}

%description
Python domain model classes for the MythX platform.

%prep
%autosetup -p1 -n mythx-models-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest --cov-report html --cov-report term --cov mythx_models tests/

%files
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/mythx_models-*.egg-info/
%{python3_sitelib}/mythx_models/

%changelog
%autochangelog
