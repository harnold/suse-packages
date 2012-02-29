%global ocamlver 3.12
%global ocamlrel 1

Name:             ocaml
Summary:          The OCaml compiler and programming environment
Version:          %{ocamlver}.%{ocamlrel}
Release:          3
License:          QPLv1.0, LGPLv2 with exceptions
Group:            Development/Languages/Other
Url:              http://caml.inria.fr/ocaml
Source0:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{version}.tar.gz
Source1:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{ocamlver}-refman.html.tar.gz
Source2:          http://caml.inria.fr/pub/distrib/ocaml-%{ocamlver}/ocaml-%{ocamlver}-refman.info.tar.gz
Patch0:           ocaml-cflags.patch
Patch1:           ocaml-info-dir.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    binutils-devel
BuildRequires:    ncurses-devel
BuildRequires:    gdbm-devel
BuildRequires:    xorg-x11-devel
BuildRequires:    tcl-devel
BuildRequires:    tk-devel
BuildRequires:    texinfo
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
gunzip infoman/ocaml.info.gz
%patch -P 1 -p1
gzip -9 infoman/ocaml.info

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
%exclude %{_bindir}/camlp4*
%exclude %{_bindir}/mkcamlp4
%exclude %{_bindir}/labltk
%exclude %{_bindir}/ocamlbrowser
%exclude %{_libdir}/ocaml/camlp4
%exclude %{_libdir}/ocaml/labltk
%exclude %{_libdir}/ocaml/stublibs/dlllabltk.so

%files doc
%defattr(-,root,root)
%doc %{_mandir}/*/*
%doc %{_infodir}/*
%doc htmlman
%exclude %{_mandir}/man1/camlp4*

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
