# Copyright 2011, 2012, 2013 Holger Arnold.
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

%global vim_sitedir     %{_datadir}/vim/site

Name: taskwarrior
Summary: Command-line todo list manager
Version: 2.2.0
Release: 2
License: MIT
Group: Productivity/Other
Url: http://taskwarrior.org/

Source0: http://www.taskwarrior.org/download/task-%{version}.tar.gz
Patch0: taskwarrior-datadir.patch

BuildRequires: cmake
BuildRequires: libuuid-devel

%description
Taskwarrior maintains a list of tasks that you want to do, allowing
you to add, remove, and otherwise manipulate them.  Taskwarrior has
a rich list of subcommands that allow you to do sophisticated things
with it.  It has customizable reports, charts, GTD features, device
synching and more.

%prep
%setup -q -n task-%{version}
%patch -P 0 -p1

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DTASK_DOCDIR=share/doc/packages/%{name} \
        -DTASK_DATADIR=share/%{name}
make %{?_smp_mflags}

%install
%make_install

# Bash completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
cp %{buildroot}/%{_datadir}/%{name}/scripts/bash/task.sh %{buildroot}%{_sysconfdir}/bash_completion.d

# Vim
install -d %{buildroot}%{vim_sitedir}/{ftdetect,syntax}
install -m 644 scripts/vim/ftdetect/*.vim %{buildroot}%{vim_sitedir}/ftdetect
install -m 644 scripts/vim/syntax/*.vim %{buildroot}%{vim_sitedir}/syntax

# Remove unused files
rm %{buildroot}%{_datadir}/%{name}/rc/refresh
rm %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*
%{_docdir}/%{name}
%{_sysconfdir}/bash_completion.d/*
%{vim_sitedir}/*/*

%changelog
* Fri Sep 06 2013 holgerar@gmail.com - 2.2.0-2
- Use correct paths in default ~/.taskrc file.

* Wed Aug 21 2013 holgerar@gmail.com - 2.2.0-1
- Update to version 2.2.0:
  * Task states such as BLOCKED, OVERDUE, WAITING, etc. can be queried
    using virtual tags.  See 'man task' for details.
  * New 'modified' task attribute.
  * Improved Bash auto-completion.
  * Improved statistics report.
  * Support for Lua extensions removed.
  * Many bugs fixed.

* Mon Nov 19 2012 holgerar@gmail.com - 2.1.2-1
- Update to version 2.1.2
- Install Vim support files
- Install add-ons, extensions, color themes, and holiday data in
  /usr/share/taskwarrior

* Mon Mar 26 2012 holgerar@gmail.com - 2.0.0-1
- Update to version 2.0.0

* Thu Mar 01 2012 holgerar@gmail.com - 2.0.0.beta5-1
- Update to version 2.0.0.beta5

* Sat Feb 11 2012 holgerar@gmail.com - 2.0.0.beta4-1
- Create package for version 2.0.0.beta4
