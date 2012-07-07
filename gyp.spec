#
# Conditional build:
%bcond_with	tests		# build without tests

%define		svnrev	1175
#define		rel		%{nil}
Summary:	Generate Your Projects
Name:		gyp
Version:	1
Release:	%{svnrev}%{?rel:.%{rel}}
License:	New BSD
Group:		Development/Building
# use get-source.sh
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	7d88a5d46b19c072809371e9c6e877d3
URL:		http://code.google.com/p/gyp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format. It's
syntax is a universal cross-platform build representation that still
allows sufficient per-platform flexibility to accommodate
irreconcilable differences.

%package -n python-%{name}
Summary:	Python module for GYP
Group:		Development/Languages/Python

%description -n python-%{name}
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format. It's
syntax is a universal cross-platform build representation that still
allows sufficient per-platform flexibility to accommodate
irreconcilable differences.

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%{?with_tests:%{__python} gyptest.py -a}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_bindir}/gyp

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/gyp
%dir %{py_sitescriptdir}/gyp/generator
%{py_sitescriptdir}/gyp/*.py[co]
%{py_sitescriptdir}/gyp/generator/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/gyp-*.egg-info
%endif
