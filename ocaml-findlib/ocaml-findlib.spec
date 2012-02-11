%global pkg findlib

Name:             ocaml-%{pkg}
Summary:          Library manager for Objective Caml
Version:          1.2.7
Release:          1
Vendor:           http://holgerarnold.net/software/
License:          see LICENSE for details
Group:            Development/Languages/Other
Url:              http://projects.camlcity.org/projects/findlib.html
Source:           http://download.camlcity.org/download/%{pkg}-%{version}.tar.gz
Patch0:           findlib-ocamldoc.patch
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
%patch -P 0 -p1
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
