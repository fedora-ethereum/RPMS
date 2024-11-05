%global pypi_name eth_account

Name:          python-%{pypi_name}
# FIXME we have to stick with this version since we don't have ckzg packages
Version:       0.11.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Account abstraction library for web3.py
License:       MIT
URL:           https://github.com/ethereum/eth-account
Source0:       %{pypi_source eth-account}
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n eth-account-%{version}

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

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
