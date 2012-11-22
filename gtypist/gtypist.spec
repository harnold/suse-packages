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

Name:               gtypist
Summary:            Universal typing tutor
Version:            2.9
Release:            1
License:            GPL-3.0
Group:              Amusements/Teaching/Other
Url:                http://www.gnu.org/software/gtypist/
Source0:            http://ftp.gnu.org/gnu/gtypist/%{name}-%{version}.tar.xz
Source1:            init-gtypist.el
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
BuildRequires:      ncurses-devel
Requires(post):     info
Requires(preun):    info

%global emacs_sitedir   %{_datadir}/emacs/site-lisp
%global emacs_startdir  %{_datadir}/emacs/site-lisp/site-start.d

%description
GNU Typist is a text mode typing tutor.  You can learn correct typing with
it and improve your skills by practicing its exercises on a regular basis.
It uses lesson "scripts" and can be easily extended.

%prep
%setup -q

%build
%configure

%install
%make_install

rm %{buildroot}%{_infodir}/dir
gzip -9 %{buildroot}%{_infodir}/*.info

install -d %{buildroot}%{emacs_startdir}
install -m 644 %{SOURCE1} %{buildroot}%{emacs_startdir}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/gtypist.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gtypist.info.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/locale/*/*/gtypist.mo
%{emacs_sitedir}/*
%{emacs_startdir}/*
%doc %{_infodir}/gtypist*
%doc %{_mandir}/*/*
%doc ChangeLog COPYING NEWS QUESTIONS README THANKS TODO

%changelog
* Wed Nov 21 2012 holgerar@gmail.com - 2.9-1
- Create package for version 2.9