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

%global pkg magit

Name:             emacs-%{pkg}
Summary:          Emacs interface to Git
Version:          1.2.0
Release:          2
License:          GPL-3.0+ and GFDL-1.2+
Group:            Productivity/Editors/Emacs
Url:              http://philjackson.github.com/magit/
Source:           http://github.com/downloads/magit/magit/%{pkg}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    emacs
BuildRequires:    makeinfo
Requires(post):   info
Requires(preun):  info
Requires:         emacs
Requires:         git-core

%description
Magit is an Emacs interface to the Git version control system.
It provides convenient access to the most common Git operations.

%global emacs_lispdir  %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d

%prep
%setup -q -n %{pkg}-%{version}

%build
make PREFIX=/usr
makeinfo magit.texi
gzip magit.info
makeinfo --html --no-split magit.texi
mv README.md README

%install
install -d %{buildroot}%{emacs_lispdir}/%{pkg}
install -m 644 magit*.el{c,} %{buildroot}%{emacs_lispdir}/%{pkg}
install -m 644 contrib/magit*.el{c,} %{buildroot}%{emacs_lispdir}/%{pkg}
install -d %{buildroot}%{emacs_startdir}
install -m 644 50magit.el %{buildroot}%{emacs_startdir}/init-%{pkg}.el
install -d %{buildroot}%{_infodir}
install -m 644 magit.info.gz %{buildroot}%{_infodir}
install -d %{buildroot}%{_bindir}
install -m 755 contrib/magit %{buildroot}%{_bindir}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/magit.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/magit.info.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README magit.html
%doc %{_infodir}/magit.info.gz
%{_bindir}/magit
%{emacs_startdir}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/*.el

%changelog
* Thu Aug 22 2013 holgerar@gmail.com - 1.2.0-2
- Change build dependency on texinfo to makeinfo.

* Mon Nov 12 2012 holgerar@gmail.com - 1.2.0-1
- Update to version 1.2.0.

* Thu Sep 06 2012 holgerar@gmail.com - 1.1.1-2
- Drop build dependency on python-markdown.

* Wed Feb 29 2012 holgerar@gmail.com - 1.1.1-1
- Update to version 1.1.1.

* Thu Feb 09 2012 holgerar@gmail.com - 1.0.0-3
- Create package for version 1.0.0.
