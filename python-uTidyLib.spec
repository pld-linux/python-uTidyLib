%define 	module uTidylib

Summary:	Python wrapper for TidyLib
Summary(pl):	Modu³ TidyLib dla Pythona
Name:		python-%{module}
Version:	0.2
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/utidylib/%{module}-%{version}.zip
# Source0-md5:	c9f16988f92ef660f46523192ef37462
URL:		http://
Requires:	python-ctypes
Requires:	tidy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uTidyLib is a Python wrapper for TidyLib. It allows you to validate
and cleanup HTML from Python.

%description -l pl
uTidyLib to modu³ Pythona obudowywuj±cy bibliotekê TidyLib. Pozwala
sprawdzaæ poprawno¶æ i czy¶ciæ HTML z poziomu Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/tidy/{test_tidy.*,*.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitescriptdir}/tidy
%{py_sitescriptdir}/tidy/*.py[co]
