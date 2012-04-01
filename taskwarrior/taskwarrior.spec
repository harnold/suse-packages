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

%global pkg     task

Name:             taskwarrior
Summary:          Command-line todo list manager
Version:          2.0.0
Release:          1
License:          MIT
Group:            Productivity/Other
Url:              http://taskwarrior.org/
Source0:          http://www.taskwarrior.org/download/%{pkg}-%{version}.tar.gz
Source1:          http://www.taskwarrior.org/download/%{pkg}-%{version}.ref.pdf
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    cmake
BuildRequires:    lua-devel >= 5.1
BuildRequires:    libuuid-devel

%description
Taskwarrior maintains a list of tasks that you want to do, allowing
you to add, remove, and otherwise manipulate them.  Taskwarrior has
a rich list of subcommands that allow you to do sophisticated things
with it.  It has customizable reports, charts, GTD features, Lua
extensions, device synching and more.

%prep
%setup -q -n %{pkg}-%{version}

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DTASK_DOCDIR=share/doc/packages/%{name}
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 -T scripts/bash/task_completion.sh %{buildroot}%{_sysconfdir}/bash_completion.d/task.sh
install -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/*

%changelog
