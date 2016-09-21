#
# Conditional build:
%bcond_with	tests		# build without tests

%define		svnrev	1602
%define		rel	3
Summary:	Generate Your Projects
Summary(pl.UTF-8):	GYP (Generate Your Projects) - narzędzie do generowania systemów budowania
Name:		gyp
# grep version= setup.py
Version:	0.1
Release:	0.svn%{svnrev}.%{rel}
License:	New BSD
Group:		Development/Building
# use get-source.sh
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	fd1809e1716f46a585684aa0fb2df897
URL:		https://gyp.gsrc.io/
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

%description -l pl.UTF-8
GYP to narzędzie generujące natywne pliki budowania dla Visual Studio,
Xcode, SCons i/lub make'a z formatu wejściowego niezależnego od
platformy. Składnia jest uniwersalną, wieloplatformową reprezentacją
reguł, która nadal pozwala na wystarczającą elastyczność dla
poszczególnych platform, aby obsłużyć różnice między nimi.

%package -n python-%{name}
Summary:	Python modules for GYP
Summary(pl.UTF-8):	Moduły Pythona module dla GYP
Group:		Development/Languages/Python

%description -n python-%{name}
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format. It's
syntax is a universal cross-platform build representation that still
allows sufficient per-platform flexibility to accommodate
poszczególnych platform, aby obsłużyć różnice między nimi.

This package contains Python modules.

%description -n python-%{name} -l pl.UTF-8
GYP to narzędzie generujące natywne pliki budowania dla Visual Studio,
Xcode, SCons i/lub make'a z formatu wejściowego niezależnego od
platformy. Składnia jest uniwersalną, wieloplatformową reprezentacją
reguł, która nadal pozwala na wystarczającą elastyczność dla
poszczególnych platform, aby obsłużyć różnice między nimi.

Ten pakiet zawiera moduły Pythona.

%prep
%setup -q -n %{name}

%build
%py_build

%{?with_tests:%{__python} gyptest.py -a}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

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
%{py_sitescriptdir}/gyp-%{version}-py*.egg-info
%endif
