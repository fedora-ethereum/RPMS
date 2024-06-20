Name:          python-mythx-models
Version:       2.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python domain model classes for the MythX platform
License:       MIT
URL:           https://github.com/ConsenSys/mythx-models
Source0:       %{pypi_source mythx-models}
Patch1:        python-mythx-models-0001-Adjust-versions.patch
Patch2:        python-mythx-models-0002-Direct-link-instead-of-redirect.patch
Patch3:        python-mythx-models-0003-Adapt-to-Pydantic-v2.patch
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
#%autosetup -p1 -n mythx-models-%{version}
%setup -q -n mythx-models-%{version}
%patch -P1 -p1
%patch -P2 -p1
%if 0%{?fedora} > 39
%patch -P3 -p1
%endif

%build
%py3_build

%install
%py3_install
# FIXME shouldn't even install it
rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
%pytest

%files
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/mythx_models-*.egg-info/
%{python3_sitelib}/mythx_models/

%changelog
%autochangelog
