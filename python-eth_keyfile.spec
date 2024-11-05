%global pypi_name eth_keyfile

Name:          python-%{pypi_name}
Version:       0.8.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for handling the encrypted keyfile format used to store private keys
License:       MIT
URL:           https://github.com/ethereum/eth-keyfile
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-eth_keyfile-0001-Fedora-use-cryptodome-explicitly.patch
Patch2:        python-eth_keyfile-0002-Relax-dependencies.patch
Patch3:        python-eth_keyfile-0003-Add-fixtures-back.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

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
PYTHONPATH=$(pwd) %pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
