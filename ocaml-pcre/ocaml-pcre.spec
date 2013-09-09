# Copyright 2009, 2013 Holger Arnold.
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

%global ocaml_sitedir %{_libdir}/ocaml/site-lib

Name: ocaml-pcre
Summary: OCaml interface to the PCRE regular expression library
Version: 7.0.2
Release: 1
License: LGPL-2.1 with exceptions
Group: Development/Languages/Other
Url: https://bitbucket.org/mmottl/pcre-ocaml
Requires: ocaml >= 3.12
Requires: ocaml-findlib >= 1.3.1
Requires: pcre

Source: https://bitbucket.org/mmottl/pcre-ocaml/downloads/pcre-ocaml-%{version}.tar.gz

BuildRequires: ocaml >= 3.12
BuildRequires: ocaml-findlib >= 1.3.1
BuildRequires: pcre-devel

%description
This OCaml library provides an interface to the PCRE (Perl-compatible
regular expressions) library.  Compared with the Str module in the
OCaml distribution, it is more powerful, much faster, and thread-safe.

%prep
%setup -q -n pcre-ocaml-%{version}

%build
./configure --prefix %{_prefix} \
            --docdir %{_defaultdocdir}/ocaml-pcre \
            --destdir %{buildroot}
make all

%install
install -d %{buildroot}%{ocaml_sitedir}/stublibs
make install OCAMLFIND_DESTDIR=%{buildroot}%{ocaml_sitedir}
for d in AUTHORS CHANGES COPYING README; do
    mv $d.* $d
done

%files
%doc AUTHORS CHANGES COPYING README
%doc examples
%{ocaml_sitedir}/pcre
%{ocaml_sitedir}/stublibs/*

%changelog
* Mon Sep 09 2013 holgerar@gmail.com - 7.0.2-1
- Update to version 7.0.2:
  * The library now works with OCaml 4.00.
  * Some minor bugs have been fixed.

* Thu Dec 17 2009 holgerar@gmail.com - 6.0.1-1
- Create package for version 6.0.1
