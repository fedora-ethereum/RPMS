Name:          python-diskcache
Version:       5.4.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Disk and file-based cache
License:       ASL 2.0
URL:           https://grantjenks.com/docs/diskcache/
# FIXME no tests shipped to pypi. Should we just grab tarball from github?
# See comments below
#Source0:       %{pypi_source diskcache}
Source:        https://github.com/grantjenks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:        python-diskcache-0001-No-more-cache-in-FetchFromCacheMiddleware.patch
BuildRequires: python3-django
BuildRequires: python3-mock
BuildRequires: python3-nose
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-django
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-diskcache}

%description
Disk and file-based cache.

%prep
%setup -q
%if 0%{?fedora} >= 39
# Modern Django 4.1.x
%patch1 -p1
%endif

%build
%py3_build

%install
%py3_install

%check
# FIXME no tests shipped to pypi. Should we just grab tarball from github?
# See comments above
%pytest

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/diskcache-*.egg-info/
%{python3_sitelib}/diskcache/

%changelog
%autochangelog
