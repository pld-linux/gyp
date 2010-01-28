#
# Conditional build:
%bcond_without	tests		# build without tests

%define		svnrev	770
%define		rel		1
Summary:	Generate Your Projects
Name:		gyp
Version:	0.1
Release:	0.%{svnrev}.%{rel}
License:	New BSD
Group:		Development/Building
# svn co http://gyp.googlecode.com/svn/trunk@770 gyp
# tar -cjf gyp-$(svnversion gyp).tar.bz2 --exclude=.svn --remove-files gyp
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	7f87d3f19fd97d17392df778128df70d
URL:		http://code.google.com/p/gyp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format. It's
syntax is a universal cross-platform build representation that still
allows sufficient per-platform flexibility to accommodate
irreconcilable differences.

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

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
%attr(755,root,root) %{_bindir}/gyp
%dir %{py_sitescriptdir}/gyp
%dir %{py_sitescriptdir}/gyp/generator
%{py_sitescriptdir}/gyp/*.py[co]
%{py_sitescriptdir}/gyp/generator/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/gyp-*.egg-info
%endif
