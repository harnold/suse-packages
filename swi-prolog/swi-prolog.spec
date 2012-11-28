# Copyright 2012 Holger Arnold.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT.  IN NO EVENT
# SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
# FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

%global pkg pl

Name:             swi-prolog
Summary:          Powerful Prolog environment
Version:          6.2.3
Release:          1
License:          LGPL-2.1
Group:            Development/Languages/Other
Url:              http://www.swi-prolog.org/
Source0:          http://www.swi-prolog.org/download/stable/src/%{pkg}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    pkg-config
BuildRequires:    gmp-devel
BuildRequires:    ncurses-devel
BuildRequires:    readline-devel
BuildRequires:    unixODBC-devel
BuildRequires:    libopenssl-devel
BuildRequires:    zlib-devel
BuildRequires:    java-devel >= 1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    xorg-x11-devel
BuildRequires:    libjpeg62-devel
Requires:         pkg-config
Obsoletes:        swipl < %{version}
Provides:         swipl = %{version}

%description
SWI-Prolog is a powerful Prolog environment.

%package doc
Summary:          Documentation for SWI-Prolog
BuildArch:        noarch
AutoReq:          no

%description doc
SWI-Prolog is a powerful Prolog environment.

This package contains the SWI-Prolog Reference Manual and documentation
for the libraries that are part of SWI-Prolog.

%package xpce
Summary:        Toolkit for developing graphical user interfaces in SWI-Prolog
Requires:       swi-prolog = %{version}-%{release}

%description xpce
XPCE is an object-oriented toolkit for developing platform-independent
graphical user interfaces in SWI-Prolog and other interactive and
dynamically typed languages.

%prep
%setup -q -n %{pkg}-%{version}

%build
./configure \
    --prefix=%{_prefix} \
    --disable-libdirversion \
    --with-world
make %{?_smp_mflags}

%install
%make_install

# Include files
install -d %{buildroot}%{_includedir}/swipl
mv %{buildroot}%{_libdir}/swipl/include/* %{buildroot}%{_includedir}/swipl

# Java files
install -d %{buildroot}%{_javadir}
rm %{buildroot}%{_libdir}/swipl/Makefile
ln -s %{_libdir}/swipl/lib/jpl.jar %{buildroot}%{_javadir}

# Reference manual and package documentation
mkdir install
mv -f %{buildroot}%{_libdir}/swipl/doc install

# Documentation for XPCE
mkdir install/xpce
mv -f %{buildroot}%{_libdir}/swipl/xpce/{COPYING,README} install/xpce

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/swipl
%{_includedir}/swipl
%{_javadir}/*
%doc COPYING README
%doc %{_mandir}/*/*
%exclude %{_bindir}/xpce-client
%exclude %{_libdir}/swipl/customize/dotxpcerc
%exclude %{_libdir}/swipl/lib/*/pl2xpce.so
%exclude %{_libdir}/swipl/xpce

%files doc
%defattr(-,root,root)
%doc install/doc/Manual
%doc install/doc/packages

%files xpce
%defattr(-,root,root)
%{_bindir}/xpce-client
%{_libdir}/swipl/customize/dotxpcerc
%{_libdir}/swipl/lib/*/pl2xpce.so
%{_libdir}/swipl/xpce
%doc install/xpce/*

%changelog
* Wed Nov 28 2012 holgerar@gmail.com - 6.2.3-1
- Update to version 6.2.3:
  * Initial version of the 'pack' package manager.
  * Better source file handling, notably wrt. ':- include(File)'.
  * Many fixes to the debugger, improving source handling
    and the logic that decides on which ports are hidden.
- Drop version number from library path.
- Move header files to /usr/include/swipl.

* Tue Mar 27 2012 holgerar@gmail.com - 6.0.2-1
- Create package for version 6.0.2.
