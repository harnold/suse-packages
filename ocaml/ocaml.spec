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

%global ocamlver 4.00
%global ocamlrel 1

Name:             ocaml
Summary:          The OCaml compiler and programming environment
Version:          %{ocamlver}.%{ocamlrel}
Release:          3
License:          QPL-1.0 with exceptions and LGPL-2.0 with exceptions
Group:            Development/Languages/Other
Url:              http://caml.inria.fr/ocaml
Source0:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{version}.tar.bz2
Source1:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{ocamlver}-refman-html.tar.gz
Source2:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{ocamlver}-refman.info.tar.gz
Patch0:           ocaml-cflags.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    binutils-devel
BuildRequires:    ncurses-devel
BuildRequires:    gdbm-devel
BuildRequires:    xorg-x11-devel
BuildRequires:    tcl-devel
BuildRequires:    tk-devel
Provides:         ocaml(compiler) = %{version}
Provides:         ocaml(runtime) = %{version}

%global __ocaml_requires_opts -c -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo"
%global __ocaml_provides_opts -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo"

%description
OCaml is a strongly typed functional programming language featuring
a sound polymorphic type system with type inference, a powerful module
system, and a fully-fledged object-oriented layer.

This package contains the OCaml runtime system, an interactive toplevel
system, bytecode and native-code compilers, the OCaml standard libraries,
lexer and parser generators, a dependency generator, a build tool,
a documentation generator, an interactive debugger, and a profiler.

%package doc
Summary:          Documentation for the OCaml system
BuildArch:        noarch
Requires(post):   info
Requires(preun):  info

%description doc
OCaml is a strongly typed functional programming language featuring
a sound polymorphic type system with type inference, a powerful module
system, and a fully-fledged object-oriented layer.

This package contains documentation for the OCaml system.

%package camlp4
Summary:          Preprocessor-pretty-printer for OCaml
Requires:         ocaml = %{version}-%{release}

%description camlp4
CamlP4 is a tool for OCaml that combines a preprocessor for the OCaml
compiler and a pretty-printer.  It can be used to redefine and extend
the syntax of the input language and to pretty-print OCaml programs
using different syntaxes.

%package labltk
Summary:          OCaml interface to the Tcl/Tk GUI library
Requires:         ocaml = %{version}-%{release}
Requires:         tcl-devel
Requires:         tk-devel

%description labltk
The labltk library provides an OCaml interface to the Tcl/Tk GUI
library.

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%patch -P 0 -p1

%build
CFLAGS="%{optflags}" ./configure \
    -prefix %{_prefix} \
    -bindir %{_bindir} \
    -libdir %{_libdir}/ocaml \
    -mandir %{_mandir}
make world.opt

%install
make install \
    BINDIR="%{buildroot}%{_bindir}" \
    LIBDIR="%{buildroot}%{_libdir}/ocaml" \
    MANDIR="%{buildroot}%{_mandir}"
install -m 644 camlp4/man/camlp4.1.tpl %{buildroot}%{_mandir}/man1/camlp4.1
install -d %{buildroot}%{_infodir}
install -m 644 infoman/ocaml.info*.gz %{buildroot}%{_infodir}

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/ocaml.info.gz

%postun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ocaml.info.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_bindir}/*
%{_libdir}/ocaml
%doc %{_mandir}/man1/*
%exclude %{_bindir}/camlp4*
%exclude %{_bindir}/mkcamlp4
%exclude %{_bindir}/labltk
%exclude %{_bindir}/ocamlbrowser
%exclude %{_libdir}/ocaml/camlp4
%exclude %{_libdir}/ocaml/labltk
%exclude %{_libdir}/ocaml/stublibs/dlllabltk.so
%exclude %{_mandir}/man1/camlp4*

%files doc
%defattr(-,root,root)
%doc %{_mandir}/man3/*
%doc %{_infodir}/*
%doc htmlman

%files camlp4
%defattr(-,root,root)
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%{_libdir}/ocaml/camlp4
%doc %{_mandir}/man1/camlp4*
%doc camlp4/examples

%files labltk
%defattr(-,root,root)
%{_bindir}/labltk
%{_bindir}/ocamlbrowser
%{_libdir}/ocaml/labltk
%{_libdir}/ocaml/stublibs/dlllabltk.so
%doc otherlibs/labltk/examples_camltk
%doc otherlibs/labltk/examples_labltk

%changelog
* Tue Aug 14 2013 holgerar@gmail.com - 4.00.1-3
- Remove build dependency on texinfo.

* Wed Nov 21 2012 holgerar@gmail.com - 4.00.1-2
- Include man pages for OCaml binaries in main package.

* Thu Nov 15 2012 holgerar@gmail.com - 4.00.1-1
- Update to version 4.00.1: Bugfix release.
- Move to SUSE's new patch format.

* Thu Sep 06 2012 holgerar@gmail.com - 4.00.0-1
- Update to version 4.00.0:
  * Generalized algebraic data types (GADTs) added to the language.
  * Improved packing and unpacking of first-class modules.
  * New compiler backend for ARM.
  * Support for randomized hash tables in the library.
  See http://caml.inria.fr/pub/distrib/ocaml-4.00/notes/Changes
  for a detailed list of changes.
- Drop ocaml-info-dir.patch: fixed upstream.

* Sat Feb 11 2012 holgerar@gmail.com - 3.12.1-2
- Create package for version 3.12.1.
