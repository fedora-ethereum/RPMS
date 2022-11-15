Name:          python-dataclassy
Version:       0.11.1
Release:       %autorelease
BuildArch:     noarch
Summary:       An enhanced, tiny reimplementation of dataclasses
License:       MPL 2.0
URL:           https://github.com/biqqles/dataclassy
Source0:       %{pypi_source dataclassy}
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-dataclassy}

%description
An enhanced, tiny reimplementation of data classes in Python - an alternative
to the built-in dataclasses module that avoids many of its common pitfalls.
dataclassy is designed to be more flexible, less verbose, and more powerful
than dataclasses, while retaining a familiar interface.

%prep
%autosetup -p1 -n dataclassy-%{version}


%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE.md
#%%doc docs
%doc README.md
%{python3_sitelib}/dataclassy/
%{python3_sitelib}/dataclassy-*.egg-info/

%changelog
%autochangelog
