Name:          python-asn1tools
Version:       0.165.0
Release:       %autorelease
BuildArch:     noarch
Summary:       ASN.1 parsing, encoding and decoding
License:       MIT
URL:           https://github.com/eerimoq/asn1tools
Source0:       %{pypi_source asn1tools}
BuildRequires: python-diskcache
BuildRequires: python3-bitstruct
BuildRequires: python3-prompt-toolkit
BuildRequires: python3-pyparsing
BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-asn1tools}

%description
ASN.1 parsing, encoding and decoding.

%prep
%autosetup -p1 -n asn1tools-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE
%doc README.rst
%{_bindir}/asn1tools
%{python3_sitelib}/asn1tools-*.egg-info/
%{python3_sitelib}/asn1tools/

%changelog
%autochangelog
