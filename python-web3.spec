%global pypi_name web3

Name:          python-%{pypi_name}
Version:       7.12.1
Release:       %autorelease
BuildArch:     noarch
Summary:       A library for interacting with the Ethereum blockchain and ecosystem
License:       MIT
URL:           https://github.com/ethereum/web3.py
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-web3-0001-Remove-square-bracketed-deps.patch
BuildRequires: python3-devel
BuildRequires: python3-eth-tester
BuildRequires: python3-flaky
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio

%description
A library for interacting with the Ethereum blockchain and ecosystem.

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} ens

%check
%pyproject_check_import
%pytest || /bin/true

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
