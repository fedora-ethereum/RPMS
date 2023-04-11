Name:          python-bitarray
Version:       2.7.3
Release:       %autorelease
Summary:       Efficient arrays of booleans for Python
License:       Python-2.0.1
URL:           https://github.com/ilanschnell/bitarray
Source0:       %{pypi_source bitarray}
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-bitarray}

%description
Efficient arrays of booleans for Python.


%prep
%autosetup -p1 -n bitarray-%{version}


%build
%py3_build

%install
%py3_install

%check
# FIXME - no pytest tests
#%%pytest

%files
%license LICENSE
#%%doc docs
%doc README.rst
%{python3_sitearch}/bitarray/
%{python3_sitearch}/bitarray-*.egg-info/

%changelog
%autochangelog
