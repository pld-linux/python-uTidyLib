%define 	module uTidylib

Summary:	Python wrapper for TidyLib
Summary(pl.UTF-8):	Moduł TidyLib dla Pythona
Name:		python-%{module}
Version:	0.2
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://download.berlios.de/utidylib/%{module}-%{version}.zip
# Source0-md5:	c9f16988f92ef660f46523192ef37462
URL:		http://utidylib.berlios.de/
BuildRequires:	python-modules
BuildRequires:	unzip
Requires:	tidy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uTidyLib is a Python wrapper for TidyLib. It allows you to validate
and cleanup HTML from Python.

%description -l pl.UTF-8
uTidyLib to moduł Pythona obudowywujący bibliotekę TidyLib. Pozwala
sprawdzać poprawność i czyścić HTML z poziomu Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/tidy/{test_tidy.*,*.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitescriptdir}/tidy
%{py_sitescriptdir}/tidy/*.py[co]
