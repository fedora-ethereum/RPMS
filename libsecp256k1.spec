%global forgeurl https://github.com/Bitcoin-ABC/secp256k1

Name:    libsecp256k1
Version: 0.27.1
Release: %autorelease
Summary: Optimized C library for EC operations on curve secp256k1

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: gmp-devel
BuildRequires: openssl-devel
BuildRequires: make

%description
%{summary}.

Includes support for Schnorr signature.

Uses the implementation maintained by Bitcoin-ABC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgesetup

%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful, even on
# architectures were the ASM is not valid when compiling with LTO.
#
# -ffat-lto-objects is sufficient to address this issue.  It is the default
# for F33, but is expected to only be enabled for packages that need it in
# F34, so we use it here explicitly
%define _lto_cflags -flto=auto -ffat-lto-objects

./autogen.sh
%configure --disable-static \
           --enable-module-recovery \
           --enable-experimental \
           --enable-module-ecdh \
           --enable-module-extrakeys \
           --enable-module-schnorrsig


%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%check
make check


%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.0*

%files devel
%license COPYING
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
