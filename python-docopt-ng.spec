# FIXME use a version from Fedora

%global pypi_name docopt-ng

Name:           python-docopt-ng
Version:        0.9.0
Release:        %autorelease
Summary:        Pythonic argument parser, that will make you smile
License:        MIT
URL:            https://github.com/jazzband/docopt-ng
Source0:        %{pypi_source docopt_ng}
Patch1:         python-docopt-ng-0001-Revert-Remerge-master-changes.patch
Patch2:         python-docopt-ng-0002-partially-revert-back-to-setuptools.patch
Patch3:         python-docopt-ng-0003-Replace-unmaintained-docopt.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-rpm-generators
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
Obsoletes:      python3-docopt
%{?python_provide:%python_provide python3-docopt-ng}

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%prep
%autosetup -n docopt_ng-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE-MIT
%doc README.md
%{python3_sitelib}/docopt-*.egg-info/
%{python3_sitelib}/docopt/
#%%{python3_sitelib}/__pycache__/docopt.*

%changelog
%autochangelog
