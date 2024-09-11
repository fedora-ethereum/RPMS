%global pypi_name hexbytes

Name:          python-%{pypi_name}
Version:       1.2.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Python `bytes` subclass that decodes hex, with a readable console output
License:       MIT
URL:           https://github.com/ethereum/hexbytes
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# wget https://raw.githubusercontent.com/ethereum/hexbytes/e940383d8cb3ab5057a1d6af66b369d247f4dfe3/tox.ini
Source1:       python-hexbytes-tox.ini
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}.

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest
# FIXME - requires internet access
#tox -r

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
