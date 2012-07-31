# Copyright 2009-2012 Holger Arnold.
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

%global pkg findlib

Name:             ocaml-%{pkg}
Summary:          Library manager for Objective Caml
Version:          1.3.1
Release:          1
License:          MIT
Group:            Development/Languages/Other
Url:              http://projects.camlcity.org/projects/findlib.html
Source:           http://download.camlcity.org/download/%{pkg}-%{version}.tar.gz
Patch1:           findlib-manpath.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    ocaml
BuildRequires:    ocaml-camlp4
BuildRequires:    ocaml-labltk
BuildRequires:    ncurses-devel
Requires:         ocaml
Requires:         ocaml-camlp4
Requires:         ocaml-labltk

%description
Findlib is a library manager for Objective Caml.  It defines a scheme for
storing libraries and additional metadata such as a version string, the
archive files comprising the library, compiler and linker options, and
dependencies on other libraries.  Findlib includes a query tool to retrieve
the stored information and frontends to the various OCaml compilers that
simplify the usage of libraries.

%prep
%setup -n %{pkg}-%{version}
%patch -P 1 -p1

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/QUICKSTART doc/README doc/guide-html doc/ref-html
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/ocaml/*

%changelog
