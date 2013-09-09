# Copyright 2009-2013 Holger Arnold.
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

Name: ocaml-findlib
Summary: Library manager for Objective Caml
Version: 1.4
Release: 1
License: MIT
Group: Development/Languages/Other
Url: http://projects.camlcity.org/projects/findlib.html
Requires: ocaml

Source: http://download.camlcity.org/download/findlib-%{version}.tar.gz
Patch0: findlib-manpath.patch

BuildRequires: ocaml
BuildRequires: ocaml-camlp4
BuildRequires: ocaml-labltk
BuildRequires: ncurses-devel

%description
Findlib is a library manager for Objective Caml.  It defines a scheme
for storing libraries and additional metadata such as a version string,
the archive files comprising the library, compiler and linker options,
and dependencies on other libraries.  Findlib includes a query tool to
retrieve the stored information and frontends to the various OCaml
compilers that simplify the usage of libraries.

%prep
%setup -n findlib-%{version}
%patch -P 0 -p1

%build
./configure -bindir %{_bindir} \
            -mandir %{_mandir} \
            -sitelib %{_libdir}/ocaml/site-lib \
            -config %{_sysconfdir}/findlib.conf \
            -with-toolbox
make all
make opt

%install
make install prefix=%{buildroot}
install -d %{buildroot}%{_libdir}/ocaml/site-lib/stublibs

%post
if [[ "$1" = 1 && -w %{_libdir}/ocaml/ld.conf ]]; then
  echo "%{_libdir}/ocaml/site-lib/stublibs" >>%{_libdir}/ocaml/ld.conf
fi

%postun
if [[ "$1" = 0 && -w %{_libdir}/ocaml/ld.conf ]]; then
  sed -i "\|%{_libdir}/ocaml/site-lib|d" %{_libdir}/ocaml/ld.conf
fi

%files
%doc doc/QUICKSTART doc/README doc/guide-html doc/ref-html
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/ocaml/*

%changelog
* Tue Aug 13 2013 holgerar@gmail.com - 1.4-1
- Update to version 1.4:
  * Improved performance when many arguments need to be processed.
  * ocamldoc.opt is configured automatically.
  * New config switch -no-custom to prevent that ocamlfind is linked
    in custom-runtime mode (bytecode only).
  * Support for ocamloptp.
  * New function Topfind.log for controlling the verbosity.
  * Rewritten Fl_metascanner without camlp4.

* Thu Nov 15 2012 holgerar@gmail.com - 1.3.3-1
- Move to SUSE's new patch format.

* Thu Sep 06 2012 holgerar@gmail.com - 1.3.3-1
- Update to version 1.3.3.

* Tue May 08 2012 holgerar@gmail.com - 1.3.1-1
- Update to version 1.3.1.

* Thu Mar 01 2012 holgerar@gmail.com - 1.2.8-1
- Update to version 1.2.8.
- Drop findlib-ocamldoc.patch: fixed upstream.

* Sat Feb 11 2012 holgerar@gmail.com - 1.2.7-1
- Create package for version 1.2.7.
