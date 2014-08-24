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

%global maj 0
%global pkg libsuil%{maj}

Name: suil
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Version: 0.8.2
Release: 1
License: ISC
Url: http://drobilla.net/software/suil/

Source: http://download.drobilla.net/suil-%{version}.tar.bz2

BuildRequires: doxygen
BuildRequires: gtk2-devel
BuildRequires: libqt4-devel
BuildRequires: lv2-devel
BuildRequires: python

%description
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

%package -n %{pkg}
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Group: System/Libraries
Provides: %{pkg} = %{version}-%{release}
Recommends: %{pkg}-gtk2_in_qt4
Recommends: %{pkg}-x11_in_qt4
Recommends: %{pkg}-qt4_in_gtk2
Recommends: %{pkg}-x11_in_gtk2

%description -n %{pkg}
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

%package -n %{pkg}-gtk2_in_qt4
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Group: System/Libraries
Requires: %{pkg} = %{version}-%{release}

%description -n %{pkg}-gtk2_in_qt4
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

This packages enables loading plugins using GTK2 UIs in Qt4 hosts.

%package -n %{pkg}-x11_in_qt4
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Group: System/Libraries
Requires: %{pkg} = %{version}-%{release}

%description -n %{pkg}-x11_in_qt4
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

This package enables loading plugins using X11 UIs in Qt4 hosts.

%package -n %{pkg}-qt4_in_gtk2
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Group: System/Libraries
Requires: %{pkg} = %{version}-%{release}

%description -n %{pkg}-qt4_in_gtk2
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

This package enables loading plugins using Qt4 UIs in GTK2 hosts.

%package -n %{pkg}-x11_in_gtk2
Summary: Lightweight C library for loading and wrapping LV2 plugin UIs
Group: System/Libraries
Requires: %{pkg} = %{version}-%{release}

%description -n %{pkg}-x11_in_gtk2
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

This package enables loading plugins using X11 UIs in GTK2 hosts.

%package -n %{pkg}-devel
Summary: Development files for Suil
Group: Development/Libraries/C and C++
Requires: %{pkg} = %{version}-%{release}

%description -n %{pkg}-devel
Suil makes it possible to load a UI of any toolkit in a host using any
other toolkit (assuming the toolkits are both supported by Suil).  Hosts
do not need to build against or link to foreign toolkit libraries to use
UIs written with that toolkit; all the necessary magic is performed by
dynamically loaded modules.

This package provides the development files for Suil.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"; \
export CXXFLAGS="%{optflags}"; \
./waf configure --prefix=%{_prefix} \
                --configdir=%{_sysconfdir} \
                --libdir=%{_libdir} \
                --docs
./waf
./waf install --destdir=%{buildroot}

gzip -9 %{buildroot}/%{_mandir}/man3/suil.3

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -n %{pkg}
%doc AUTHORS COPYING NEWS README
%{_libdir}/libsuil-%{maj}.so.*
%dir %{_libdir}/suil-%{maj}

%files -n %{pkg}-gtk2_in_qt4
%{_libdir}/suil-%{maj}/libsuil_gtk2_in_qt4.so

%files -n %{pkg}-x11_in_qt4
%{_libdir}/suil-%{maj}/libsuil_x11_in_qt4.so

%files -n %{pkg}-qt4_in_gtk2
%{_libdir}/suil-%{maj}/libsuil_qt4_in_gtk2.so

%files -n %{pkg}-x11_in_gtk2
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk2.so

%files -n %{pkg}-devel
%{_includedir}/suil-%{maj}
%{_libdir}/libsuil-%{maj}.so
%{_libdir}/pkgconfig/suil-%{maj}.pc
%{_datadir}/doc/suil-%{maj}
%{_mandir}/man3/suil.3.gz

%changelog
* Sun Aug 24 2014 holgerar@gmail.com - 0.8.2-1
- Create package for version 0.8.2.
