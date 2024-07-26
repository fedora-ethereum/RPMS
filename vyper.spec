%global git_commit e9db8d9f7486eae38f5b86531629019ad28f514e


Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.4.0
Release:	%autorelease
BuildArch:	noarch
License:	Apache-2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source %{name}}
Patch1:		vyper-0001-Use-Cryptodomex.patch
Patch2:		vyper-0002-Ease-version-requirements.patch
BuildRequires:	git
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	sed

%description
%{summary}.

%prep
%autosetup -p1
echo ${git_commit:0:7} > "./vyper_git_commithash.txt"

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
#rm -f %{buildroot}/usr/vyper_git_commithash.txt
#rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
%pyproject_check_import
# FIXME not enough dependencies
#%%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/fang
%{_bindir}/vyper
%{_bindir}/vyper-json
%{_bindir}/vyper-serve

%changelog
%autochangelog
