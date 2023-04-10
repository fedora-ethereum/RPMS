Name:          python-ipfshttpclient
Version:       0.8.0
Release:       0.a2.%autorelease
BuildArch:     noarch
Summary:       A python client library for the IPFS API
License:       MIT
URL:           https://github.com/ipfs-shipyard/py-ipfs-http-client
Source0:       https://files.pythonhosted.org/packages/source/i/ipfshttpclient/ipfshttpclient-0.8.0a2.tar.gz
#Source0:       %{pypi_source ipfshttpclient}
BuildRequires: python-multiaddr
BuildRequires: python3-flit-core
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: tox
%{?python_provide:%python_provide python3-ipfshttpclient}

%description
A python client library for the IPFS API.

%prep
%autosetup -p1 -n ipfshttpclient-%{version}a2

%build
%py3_build

%install
%py3_install

%check
# FIXME
#%%pytest
#tox

%files
%license LICENSE
%doc README.md RELEASE.md
%{python3_sitelib}/ipfshttpclient/
%{python3_sitelib}/ipfshttpclient-*.egg-info

%changelog
%autochangelog
