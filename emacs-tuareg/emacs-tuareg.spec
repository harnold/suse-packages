# Copyright 2009-2012 Holger Arnold.
#
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the author be held liable for any damages arising from the
# use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.

%global pkg tuareg

Name:             emacs-%{pkg}
Summary:          OCaml editing mode for Emacs
Version:          2.0.4
Release:          4
License:          GPL-2.0+
Group:            Productivity/Editors/Emacs
Url:              http://tuareg.forge.ocamlcore.org/
Source0:          https://forge.ocamlcore.org/frs/download.php/514/%{pkg}-%{version}.tgz
Source1:          https://forge.ocamlcore.org/frs/download.php/516/tuareg-caml-mode.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    emacs
Requires:         emacs

%description
Tuareg is an OCaml editing mode for Emacs.  It provides automatic
indentation and highlighting of Objective Caml sources and supports
running an OCaml toplevel and the OCaml debugger from within Emacs.

%global emacs_lispdir  %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d

%prep
%setup -q -T -b 0 -n %{pkg}-%{version}
%setup -q -T -D -a 1 -n %{pkg}-%{version}

%build
mv tuareg-caml-mode/*.el .
emacs --no-init-file --no-site-file --batch -L . -f batch-byte-compile \
    caml-emacs.el caml-help.el caml-types.el tuareg.el camldebug.el

%install
install -d %{buildroot}%{emacs_lispdir}/%{pkg}
install -m 644 \
    caml-emacs.el{c,} caml-help.el{c,} caml-types.el{c,} \
    tuareg.el{c,} camldebug.el{c,} \
    %{buildroot}%{emacs_lispdir}/%{pkg}
install -d %{buildroot}%{emacs_startdir}
install -m 644 append-tuareg.el %{buildroot}%{emacs_startdir}/init-%{pkg}.el

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING HISTORY README
%{emacs_startdir}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/*.el

%changelog
