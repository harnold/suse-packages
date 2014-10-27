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

Name: notmuch
Summary: Thread-based email index, search and tagging
Version: 0.18.2
Release: 1
License: GPL-3.0+
Group: Productivity/Networking/Email/Utilities
Url: http://notmuchmail.org

Source:http://notmuchmail.org/releases/notmuch-%{version}.tar.gz

BuildRequires: emacs
BuildRequires: glib2-devel
BuildRequires: gmime-devel
BuildRequires: libtalloc-devel
BuildRequires: libxapian-devel
BuildRequires: perl
BuildRequires: python-Sphinx
BuildRequires: zlib-devel

%description
Notmuch is a system for indexing, searching, reading, and tagging large
collections of email messages in maildir or mh format.  It uses the Xapian
library to provide fast, full-text search with a convenient search syntax.

%package emacs
Summary: Notmuch mail client for Emacs
Requires: emacs
BuildArch: noarch

%description emacs
This package contains the notmuch mail client for Emacs.

%package mutt
Summary: Notmuch integration for Mutt
Requires: mutt
Requires: perl(Mail::Internet)
Requires: perl(String::ShellQuote)
Requires: perl(Term::ReadLine)
BuildArch: noarch

# Currently only available in devel:languages:perl
Requires: perl(Mail::Box)

%description mutt
This package enables stating a search query interactively and then jump to a
fresh Maildir containing its search results only, as well as to reconstruct
threads on the fly starting from the currently highlighted mail.

Check the manpage for the 2-liner configuration snippet for your Mutt
configuration files (~/.muttrc, /etc/Muttrc, or a /etc/Muttrc.d snippet).

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir}
make %{?_smp_flags}

%install
%make_install

install -d %{buildroot}%{_bindir}
install -m 755 contrib/notmuch-mutt/notmuch-mutt %{buildroot}%{_bindir}

%files
%doc AUTHORS COPYING COPYING-GPL-3 NEWS README
%{_bindir}/notmuch
%{_datadir}/zsh/functions/Completion/Unix/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*/*
%{_sysconfdir}/bash_completion.d/*

%files emacs
%{_datadir}/emacs/site-lisp/*

%files mutt
%doc contrib/notmuch-mutt/README
%doc contrib/notmuch-mutt/notmuch-mutt.rc
%{_bindir}/notmuch-mutt

%changelog
* Mon Oct 27 2014 holgerar@gmail.com - 0.18.2-1
- Create package for version 0.18.2.
