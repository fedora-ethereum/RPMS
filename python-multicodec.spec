Name:          python-multicodec
Version:       0.2.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Multicodec implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-multicodec
Source0:       %{pypi_source py-multicodec}
BuildRequires: python-morphys
BuildRequires: python-varint
BuildRequires: python3-pip
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-wheel
%{?python_provide:%python_provide python3-multicodec}

%description
Multicodec implementation in Python.

%prep
%autosetup -p1 -n py-multicodec-%{version}

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python3_sitelib}/multicodec/
%{python3_sitelib}/py_multicodec-*.egg-info/

%changelog
%autochangelog
