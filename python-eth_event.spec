%global pypi_name eth_event

Name:          python-%{pypi_name}
Version:       1.2.5
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for Ethereum event decoding and topic generation.
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/eth-event
Source0:       %{pypi_source eth-event}
Patch1:        python-eth_event-0001-Readd-missing-test-files.patch
Patch2:        python-eth_event-0002-Relax-deps.patch
Patch3:        python-eth_event-0003-Adjust-tests-for-hexbytes-1.0.0.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n eth-event-%{version}

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
