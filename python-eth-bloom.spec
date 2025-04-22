%global pypi_name eth_bloom

Name:          python-eth-bloom
Version:       3.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       An implementation of the Ethereum bloom filter
License:       MIT
URL:           https://github.com/ethereum/eth-bloom
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eth-bloom-0001-Relax-deps.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-bloom
Summary: %{summary}

%description -n python3-eth-bloom
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-bloom -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
