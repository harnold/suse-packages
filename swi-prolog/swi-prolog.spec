# Copyright 2012 Holger Arnold.
#
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the author be held liable for any damages arising from the
# use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.

%global pkg pl

Name:             swi-prolog
Summary:          Powerful Prolog environment
Version:          6.0.2
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
Provides:         swipl

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
Summary:          Toolkit for developing graphical user interfaces in SWI-Prolog
Requires:         swi-prolog = %{version}-%{release}

%description xpce
XPCE is an object-oriented toolkit for developing platform-independent
graphical user interfaces in SWI-Prolog and other interactive and
dynamically typed languages.

%prep
%setup -q -n %{pkg}-%{version}

%build
./configure --prefix=%{_prefix} --with-world
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_javadir}
rm %{buildroot}%{_libdir}/swipl-%{version}/Makefile
ln -s %{_libdir}/swipl-%{version}/lib/jpl.jar %{buildroot}%{_javadir}
mkdir install
mv -f %{buildroot}%{_libdir}/swipl-%{version}/doc install
mkdir install/xpce
mv -f %{buildroot}%{_libdir}/swipl-%{version}/xpce/{COPYING,README} install/xpce

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/swipl-%{version}
%{_javadir}/*
%doc COPYING README
%doc %{_mandir}/*/*
%exclude %{_bindir}/xpce-client
%exclude %{_libdir}/swipl-%{version}/customize/dotxpcerc
%exclude %{_libdir}/swipl-%{version}/lib/*/pl2xpce.so
%exclude %{_libdir}/swipl-%{version}/xpce

%files doc
%defattr(-,root,root)
%doc install/doc/Manual
%doc install/doc/packages

%files xpce
%defattr(-,root,root)
%{_bindir}/xpce-client
%{_libdir}/swipl-%{version}/customize/dotxpcerc
%{_libdir}/swipl-%{version}/lib/*/pl2xpce.so
%{_libdir}/swipl-%{version}/xpce
%doc install/xpce/*

%changelog
