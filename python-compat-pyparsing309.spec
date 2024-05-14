Name:           python-compat-pyparsing309
Version:        3.0.9
Release:        %autorelease
Summary:        Python package with an object-oriented approach to text processing

License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        %{url}/archive/pyparsing_%{version}/pyparsing-%{version}.tar.gz

BuildRequires: python3-pytest
BuildRequires: python3-rpm-generators
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
Conflicts: python3-pyparsing
BuildArch:      noarch

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%prep
%autosetup -p1 -n pyparsing-pyparsing_%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyparsing

%check
%pytest -v

%files -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst

%changelog
%autochangelog
