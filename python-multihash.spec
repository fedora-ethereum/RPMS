Name:          python-multihash
Version:       2.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Multihash implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-multihash
Source0:       %{pypi_source py-multihash}
BuildRequires: python-base58
BuildRequires: python-morphys
BuildRequires: python-varint
BuildRequires: python3-pytest
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-wheel
%{?python_provide:%python_provide python3-multihash}

%description
Multihash implementation in Python.

%prep
%autosetup -p1 -n py-multihash-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/multihash/
%{python3_sitelib}/py_multihash-*.egg-info/

%changelog
%autochangelog
