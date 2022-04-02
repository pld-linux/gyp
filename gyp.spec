#
# Conditional build:
%bcond_with	tests		# build without tests
%bcond_with	python3		# build with python 2.x

%define		gitrev	e87d37d6
%define		rel	1
Summary:	Generate Your Projects
Summary(pl.UTF-8):	GYP (Generate Your Projects) - narzędzie do generowania systemów budowania
Name:		gyp
# grep version= setup.py
Version:	0.1
Release:	1.%{rel}.%{gitrev}
License:	New BSD
Group:		Development/Building
# use get-source.sh
Source0:	%{name}-%{version}-git%{gitrev}.tar.xz
# Source0-md5:	9b6f6c10bb8def91e26c17f0be1f7f90
Patch0:         gyp-rpmoptflags.patch
Patch1:         gyp-ninja-build.patch
Patch2:         gyp-python3.patch
Patch3:         gyp-python38.patch
Patch4:         gyp-fix-cmake.patch
Patch5:         gyp-python39.patch
URL:		https://gyp.gsrc.io/
%{!?with_python3:BuildRequires:	python-devel}
%{?with_python3:BuildRequires:	python3-devel}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%{!?with_python3:Requires:	python-%{name} = %{version}-%{release}}
%{?with_python3:Requires:	python3-%{name} = %{version}-%{release}}
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

%package -n python3-%{name}
Summary:	Python modules for GYP
Summary(pl.UTF-8):	Moduły Pythona module dla GYP
Group:		Development/Languages/Python

%description -n python3-%{name}
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format. It's
syntax is a universal cross-platform build representation that still
allows sufficient per-platform flexibility to accommodate
poszczególnych platform, aby obsłużyć różnice między nimi.

This package contains Python modules.

%description -n python3-%{name} -l pl.UTF-8
GYP to narzędzie generujące natywne pliki budowania dla Visual Studio,
Xcode, SCons i/lub make'a z formatu wejściowego niezależnego od
platformy. Składnia jest uniwersalną, wieloplatformową reprezentacją
reguł, która nadal pozwala na wystarczającą elastyczność dla
poszczególnych platform, aby obsłużyć różnice między nimi.

Ten pakiet zawiera moduły Pythona.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%if %{with python3}
%py3_build
%else
%py_build
%endif

%{?with_tests:%{__python} gyptest.py -a}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%else
%py_install
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_bindir}/gyp

%if %{with python3}
%files -n python3-%{name}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/gyp
%dir %{py3_sitescriptdir}/gyp/generator
%{py3_sitescriptdir}/gyp/*.py
%{py3_sitescriptdir}/gyp/__pycache__
%{py3_sitescriptdir}/gyp/generator/*.py
%{py3_sitescriptdir}/gyp/generator/__pycache__
%{py3_sitescriptdir}/gyp-%{version}-py*.egg-info
%endif

%if !%{with python3}
%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/gyp
%dir %{py_sitescriptdir}/gyp/generator
%{py_sitescriptdir}/gyp/*.py[co]
%{py_sitescriptdir}/gyp/generator/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/gyp-%{version}-py*.egg-info
%endif
%endif
