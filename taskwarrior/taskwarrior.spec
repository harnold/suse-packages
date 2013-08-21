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

%global pkg task

Name:           taskwarrior
Summary:        Command-line todo list manager
Version:        2.2.0
Release:        1
License:        MIT
Group:          Productivity/Other
Url:            http://taskwarrior.org/
Source0:        http://www.taskwarrior.org/download/%{pkg}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  libuuid-devel

%global vim_sitedir     %{_datadir}/vim/site
%global task_datadir    %{_datadir}/%{name}

%description
Taskwarrior maintains a list of tasks that you want to do, allowing
you to add, remove, and otherwise manipulate them.  Taskwarrior has
a rich list of subcommands that allow you to do sophisticated things
with it.  It has customizable reports, charts, GTD features, device
synching and more.

%prep
%setup -q -n %{pkg}-%{version}

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DTASK_DOCDIR=share/doc/packages/%{name}
make %{?_smp_mflags}

%install
%make_install

# Install data files
install -d %{buildroot}/%{task_datadir}
mv %{buildroot}%{_docdir}/%{name}/scripts/add-ons %{buildroot}%{task_datadir}
mv %{buildroot}%{_docdir}/%{name}/i18n %{buildroot}%{task_datadir}
mv %{buildroot}%{_docdir}/%{name}/rc %{buildroot}%{task_datadir}
sed -i "s|\.\./\.\./scripts|%{task_datadir}|" %{buildroot}%{task_datadir}/rc/refresh

# Bash completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}/%{_docdir}/%{name}/scripts/bash/task.sh %{buildroot}%{_sysconfdir}/bash_completion.d

# Vim
install -d %{buildroot}%{_datadir}/vim/site/{ftdetect,syntax}
install -m 644 scripts/vim/ftdetect/*.vim %{buildroot}%{vim_sitedir}/ftdetect
install -m 644 scripts/vim/syntax/*.vim %{buildroot}%{vim_sitedir}/syntax

# Reference documentation
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 doc/ref/task-ref.pdf %{buildroot}%{_docdir}/%{name}

# Remove unused files
rm -r %{buildroot}%{_docdir}/%{name}/scripts
rm %{buildroot}%{_docdir}/%{name}/INSTALL

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*
%{_docdir}/%{name}
%{_sysconfdir}/bash_completion.d/*
%{vim_sitedir}/*/*

%changelog
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
