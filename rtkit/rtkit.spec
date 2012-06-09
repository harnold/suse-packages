# Copyright 2011, 2012 Holger Arnold.
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

Name:             rtkit
Summary:          Realtime Policy and Watchdog Daemon
Version:          0.11
Release:          1
License:          GPL-3.0+ and MIT
Group:            System/Base
Url:              http://git.0pointer.de/?p=rtkit.git
Source:           http://0pointer.de/public/%{name}-%{version}.tar.xz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    dbus-1-devel
BuildRequires:    libcap-devel
BuildRequires:    polkit-devel
Requires:         polkit
Requires:         dbus-1
Requires:         systemd

%description
RealtimeKit is a D-Bus system service that changes the scheduling
policy of processes and threads to SCHED_RR on request.  It provides
a safe way to enable real-time scheduling for unprivileged processes.

%prep
%setup -q

%build
%configure --docdir=%{_defaultdocdir} \
           --with-systemdsystemunitdir=/lib/systemd/system
make %{?_smp_mflags}
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
%make_install
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml
install -D org.freedesktop.RealtimeKit1.xml \
    %{buildroot}%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml

%clean
rm -rf %{buildroot}

%pre
groupadd -r rtkit &>/dev/null || :
/usr/bin/id rtkit >/dev/null 2>&1 || \
    useradd -r -g rtkit -c 'RealtimeKit' -s /bin/false -d /proc rtkit

%post
if [ $1 -eq 1 ]; then
    /bin/systemctl enable rtkit.service >/dev/null 2>&1 || :
fi
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%preun
if [ "$1" -eq 0 ]; then
    /bin/systemctl --no-reload disable rtkit-daemon.service >/dev/null 2>&1 || :
    /bin/systemctl stop rtkit-daemon.service >/dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%files
%defattr(0644,root,root,0755)
%doc README GPL LICENSE rtkit.c rtkit.h
%attr(0755,root,root) %{_sbindir}/rtkitctl
%attr(0755,root,root) %{_libexecdir}/rtkit-daemon
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
/lib/systemd/system/rtkit-daemon.service
%{_mandir}/man8/*

%changelog
