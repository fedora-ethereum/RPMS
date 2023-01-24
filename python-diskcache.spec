Name:          python-diskcache
Version:       0.7.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Disk and file-based cache
License:       ASL 2.0
URL:           https://grantjenks.com/docs/diskcache/
Source0:       %{pypi_source diskcache}
BuildRequires: python3-mock
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-diskcache}

%description
Disk and file-based cache.

%prep
%autosetup -p1 -n diskcache-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/asn1tools-*.egg-info/
%{python3_sitelib}/asn1tools/

%changelog
%autochangelog
