# Copyright 2011, 2012 Holger Arnold.
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

Name:             rtkit
Summary:          Realtime Policy and Watchdog Daemon
Version:          0.11
Release:          2
License:          GPL-3.0+ and MIT
Group:            System/Base
Url:              http://git.0pointer.de/?p=rtkit.git
Source:           http://0pointer.de/public/%{name}-%{version}.tar.xz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    dbus-1-devel
BuildRequires:    libcap-devel
BuildRequires:    polkit-devel
BuildRequires:    systemd
Requires:         polkit
Requires:         dbus-1
%{?systemd_requires}

%description
RealtimeKit is a D-Bus system service that changes the scheduling
policy of processes and threads to SCHED_RR on request.  It provides
a safe way to enable real-time scheduling for unprivileged processes.

%prep
%setup -q

%build
%configure \
    --docdir=%{_defaultdocdir} \
    --libexecdir=%{_libexecdir}/rtkit \
    --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
%make_install
install -D org.freedesktop.RealtimeKit1.xml \
    %{buildroot}%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml

%clean
rm -rf %{buildroot}

%pre
groupadd -r rtkit &>/dev/null || :
/usr/bin/id rtkit >/dev/null 2>&1 || \
    useradd -r -g rtkit -c 'RealtimeKit' -s /bin/false -d /proc rtkit
%service_add_pre rtkit-daemon.service

%post
%service_add_post rtkit-daemon.service
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%preun
%service_del_preun rtkit-daemon.service

%postun
%service_del_postun rtkit-daemon.service

%files
%defattr(0644,root,root,0755)
%doc README GPL LICENSE rtkit.c rtkit.h
%attr(0755,root,root) %{_sbindir}/rtkitctl
%dir %{_libexecdir}/rtkit
%attr(0755,root,root) %{_libexecdir}/rtkit/rtkit-daemon
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%{_unitdir}/rtkit-daemon.service
%{_mandir}/man8/*

%changelog
