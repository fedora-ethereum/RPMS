%global pypi_name pyunormalize

Name:          python-%{pypi_name}
Version:       16.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Unicode normalization forms (NFC, NFKC, NFD, NFKD)
License:       MIT AND Unicode-3.0
URL:           https://github.com/mlodewijck/pyunormalize
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-devel
BuildRequires: python3-pytest

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
# FIXME no tests in PyPi. Tests require ~32.67 Mbytes test data
#%%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
