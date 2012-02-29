%global pkg     task
%global pkgver  2.0.0

Name:             taskwarrior
Summary:          Command-line todo list manager
Version:          %{pkgver}.beta5
Release:          1
License:          MIT
Group:            Productivity/Other
Url:              http://taskwarrior.org/
Source0:          http://www.taskwarrior.org/download/%{pkg}-%{version}.tar.gz
Source1:          http://www.taskwarrior.org/download/%{pkg}-%{pkgver}.ref.pdf
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
