Name:          python-cid
Version:       0.3.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Self-describing content-addressed identifiers
License:       MIT
URL:           https://github.com/ipld/py-cid
Source0:       %{pypi_source py-cid}
BuildRequires: python-base58
BuildRequires: python-morphys
BuildRequires: python-multibase
BuildRequires: python-multicodec
BuildRequires: python-multihash
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-wheel
BuildRequires: sed
%{?python_provide:%python_provide python3-cid}

%description
Self-describing content-addressed identifiers for distributed systems
implementation in Python.

%prep
%autosetup -p1 -n py-cid-%{version}
sed -i -e "s,1.0.2\,<2.0,1.0.2,g;s,0.2.0\,<1.0.0,0.2.0,g" setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/cid/
%{python3_sitelib}/py_cid-*.egg-info/

%changelog
%autochangelog
