Name:          python-base58
Version:       2.1.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Base58 and Base58Check implementation
License:       MIT
URL:           https://github.com/keis/base58
Source0:       %{pypi_source base58}
BuildRequires: python3-hamcrest
BuildRequires: python3-pytest
BuildRequires: python3-pytest-benchmark
BuildRequires: python3-pytest-cov
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-base58}

%description
Base58 and Base58Check implementation compatible with what is used by the bitcoin network.

%prep
%autosetup -p1 -n base58-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license COPYING
%doc README.md
%{_bindir}/base58
%{python3_sitelib}/base58-*.egg-info/
%{python3_sitelib}/base58/

%changelog
%autochangelog
