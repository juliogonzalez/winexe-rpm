# norootforbuild

Summary: winexe
Name: winexe
Version: 1.1
Release: 1b787d2.2%{?dist}
License: GPL3
Group: Administration/Network
Source: %{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: libtalloc-devel
BuildRequires: samba4-devel >= 4.2.0
BuildRequires: popt-devel
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Requires: samba4-libs >= 4.2.0
Patch0: samba4-libs.patch
patch1: samba42-debug.patch

%description
Winexe remotely executes commands on Windows
NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux (and possibly also
from other Unices capable of building the Samba 4 software package).

%prep
%setup -q
%patch0 -p0 -b .patch0
# Disable debug only for EL >= 7 because of https://sourceforge.net/p/winexe/bugs/77/
# Patch from Michael Stowe: https://sourceforge.net/u/mstowe/winexe/ci/master/tree/
%if 0%{?rhel} >= 7
%patch1 -p0 -b .patch1
%endif

%build
cd source
./waf configure build

%install
echo %{buildroot}
rm -rf %{buildroot}
%__install -d %{buildroot}/usr/bin
%__install source/build/winexe %{buildroot}/usr/bin

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/winexe

%changelog
* Sun Jun 05 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1-1b787d2.2
- Support CentOS7 again thanks to a patch from Michel Stowe at
  https://sourceforge.net/u/mstowe/winexe/ci/master/tree

* Sun Jun 05 2016 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1-1b787d2.1
- Require Samba 4.2 as a minimum.
- Change waf script so it can use the new samba 4.x library names

* Tue Oct 20 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.1-1b787d2
- 1.1b787d2 build from http://sourceforge.net/p/winexe/winexe-waf/ci/b787d2a2c4b1abc3653bad10aec943b8efcd7aab
