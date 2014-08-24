# Copyright 2014 Holger Arnold.
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

Name: liblo
Summary: Lightweight implementation of the OSC protocol
Version: 0.28
Release: 1
License: LGPL-2.1+
Group: System/Libraries
Url: http://liblo.sourceforge.net

Source: http://downloads.sourceforge.net/liblo/liblo-%{version}.tar.gz

%description
liblo is a lightweight library that provides an easy to use implementation
of the OpenSound Control (OSC) protocol, which is a protocol for communication
among computers, sound synthesizers, and other multimedia devices that is
optimized for modern networking technology and has been used in many
application areas.

For more information, see http://www.cnmat.berkeley.edu/OpenSoundControl
or http://www.opensoundcontrol.org.

%package devel
Summary: Development files for liblo
Group: Development/Languages/C and C++

%description devel
This package provides the development files for liblo.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
%{_libdir}/liblo.so.*
%doc AUTHORS COPYING NEWS README

%files devel
%{_includedir}/lo
%{_libdir}/liblo.so
%{_libdir}/liblo.la
%{_libdir}/pkgconfig/liblo.pc

%changelog
* Sun Aug 24 2014 holgerar@gmail.com - 0.28-1
- Create package for version 0.28.
