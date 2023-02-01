%global git_hash e14f27147bd4ffc63e2bf46a68e0d271fad0ed79
%undefine _package_note_file

Summary:	Object-oriented, high-level language for implementing smart contracts
Name:		solidity
Version:	0.8.18
Release:	1%{?dist}
URL:		https://docs.soliditylang.org/
Source0:	https://github.com/ethereum/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
# Fedora-specific
Patch1:		solidity-0001-Use-system-wide-libs.patch
Patch2:		solidity-0002-Stop-checking-for-jsoncpp-version.patch
Patch3:		solidity-0003-Continue-on-big-endians.patch
Patch4:		solidity-0004-Initialize-vars-before-use.patch
Patch5:		solidity-0005-Workaround-for-compiler-s-issue.patch
Patch6:		solidity-0006-Use-static-linking-for-internal-libs.patch
Patch7:		solidity-0007-libsolutil-Add-missing-include.patch
Patch8:		solidity-0008-libsmtutil-Explicitly-use-derived-operator-from-base.patch
Patch9:		solidity-0009-libsolutil-Add-missing-include.patch

%ifarch s390x
#FIXME
%endif


BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	cvc4-devel
BuildRequires:	fmt-devel
BuildRequires:	gcc-c++
# Should be dependency of cvc4
BuildRequires:	gmp-devel
# Should be dependency of cvc4
BuildRequires:	symfpu-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	range-v3-devel
BuildRequires:	z3-devel


%description
Solidity is an object-oriented, high-level language for implementing smart
contracts. Smart contracts are programs which govern the behaviour of accounts
within the Ethereum state.


%prep
%autosetup -p1
echo %{git_hash} > commit_hash.txt


%build
#-DUSE_LD_GOLD:BOOL=OFF
%{cmake} \
	-DBoost_USE_STATIC_LIBS:BOOL=OFF \
	-DSTRICT_Z3_VERSION:BOOL=OFF \
	-DTESTS:BOOL=OFF
%cmake_build


%install
%cmake_install


%files
%{_bindir}/solc
%{_bindir}/solidity-upgrade
%{_bindir}/yul-phaser
%doc README.md
%doc SECURITY.md
%license LICENSE.txt


%changelog
%autochangelog
