Name:          python-hexbytes
Version:       0.3.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python `bytes` subclass that decodes hex, with a readable console output
License:       MIT
URL:           https://github.com/ethereum/hexbytes
Source0:       %{pypi_source hexbytes}
# wget https://raw.githubusercontent.com/ethereum/hexbytes/e940383d8cb3ab5057a1d6af66b369d247f4dfe3/tox.ini
Source1:       python-hexbytes-tox.ini
BuildRequires: python-eth_utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-towncrier
BuildRequires: tox
%{?python_provide:%python_provide python3-hexbytes}

%description
Python `bytes` subclass that decodes hex, with a readable console output.

%prep
%autosetup -p1 -n hexbytes-%{version}
install -D -p -m 0644 %{SOURCE1} ./tox.ini

%build
%py3_build

%install
%py3_install

%check
# FIXME - no pytest tests
#%%pytest
tox -r

%files
%license LICENSE
#%%doc docs
%doc README.md
%{python3_sitelib}/hexbytes/
%{python3_sitelib}/hexbytes-*.egg-info/

%changelog
%autochangelog
