%global pypi_name eth-brownie

Summary:       A framework for smart contracts for EVM
Name:          brownie
Version:       1.20.7
Release:       %autorelease
BuildArch:     noarch
License:       Apache-2.0
URL:           https://github.com/eth-brownie/brownie
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:        brownie-0001-Drop-bundled-docopt-ng.patch
Patch2:        brownie-0002-Drop-bundled-toposort.patch
Patch3:        brownie-0003-Relax-deps.patch
Patch4:        brownie-0004-Adjust-to-a-modern-Web3.py.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
A Python-based development and testing framework for smart contracts targeting
the Ethereum Virtual Machine.

%prep
%autosetup -p1 -n %{name}-%{version}
# FIXME we do not rely on pre-generated requirements.txt
cp -arv requirements.in requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%pyproject_check_import
#%%pytest

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/brownie

%changelog
%autochangelog
