Name:          python-multiaddr
Version:       0.0.9
Release:       %autorelease
BuildArch:     noarch
Summary:       Multiaddr implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-multiaddr
Source0:       %{pypi_source multiaddr}
BuildRequires: python-base58
BuildRequires: python-cid
BuildRequires: python-multicodec
BuildRequires: python-varint
BuildRequires: python3-netaddr
BuildRequires: python3-pip
BuildRequires: python3-pytest-runner
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
%{?python_provide:%python_provide python3-multiaddr}

%description
Multiaddr implementation in Python.

%prep
%autosetup -p1 -n multiaddr-%{version}

%build
%py3_build

%install
%py3_install

%check
#%%pytest

%files
%doc AUTHORS HISTORY.rst README.rst
%{python3_sitelib}/multiaddr/
%{python3_sitelib}/multiaddr-*.egg-info/

%changelog
%autochangelog
