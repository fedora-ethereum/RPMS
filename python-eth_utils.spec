%global pypi_name eth_utils

Name:          python-%{pypi_name}
Version:       5.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Utility functions for working with ethereum related codebases
License:       MIT
URL:           https://github.com/ethereum/eth-utils
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-eth_utils-0001-Just-use-eth-hash.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
#BuildRequires: python3-mypy
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
#rm -rf ./tests/mypy
rm -rf ./tests/core/functional-utils/test_type_inference.py

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
