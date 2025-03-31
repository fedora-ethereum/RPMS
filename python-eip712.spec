%global pypi_name eip712

Name:          python-%{pypi_name}
Version:       0.2.11
Release:       %autorelease
BuildArch:     noarch
Summary:       Message classes for typed structured data hashing and signing in Ethereum
License:       Apache-2.0
URL:           https://github.com/ApeWorX/eip712
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eip712-0001-Accept-more-recent-dataclassy.patch
Patch:         python-eip712-0002-Relax-setuptools-requirement.patch
Patch:         python-eip712-0003-fix-corrects-list-EIP712Type.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-xdist

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
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
