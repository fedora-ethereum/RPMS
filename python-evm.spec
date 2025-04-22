%global pypi_name py_evm
%global pre_release_tag beta.1
%global pre_release_tag_short b1

Name:          python-evm
Version:       0.12.0
Release:       %autorelease -e %{pre_release_tag}
BuildArch:     noarch
Summary:       A Python implementation of the Ethereum Virtual Machine
License:       MIT
URL:           https://github.com/ethereum/py-evm
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name %{version}%{pre_release_tag_short}}
Patch:         python-evm-0001-Fedora-use-cryptodome-explicitly.patch
BuildRequires: python3-devel
BuildRequires: python3-factory-boy
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-evm
Summary: %{summary}

%description -n python3-evm
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}%{pre_release_tag_short}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l eth

%check
%pyproject_check_import
# FIXME requires ~4 Gbytes of test data
#%%pytest

%files -n python3-evm -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
