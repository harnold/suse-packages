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

%global emacs_lispdir  %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d

Name: emacs-tuareg
Summary: OCaml editing mode for Emacs
Version: 2.0.6
Release: 1
License: GPL-2.0+
Group: Productivity/Editors/Emacs
Url: http://tuareg.forge.ocamlcore.org/
Requires: emacs
Requires: ocaml-emacs

Source0: http://forge.ocamlcore.org/frs/download.php/514/tuareg-%{version}.tar.gz

BuildArch: noarch
BuildRequires: emacs

%description
Tuareg is an OCaml editing mode for Emacs.  It provides automatic
indentation and highlighting of Objective Caml sources and supports
running an OCaml toplevel and the OCaml debugger from within Emacs.

%prep
%setup -q -n tuareg-%{version}

%build
rm tuareg-pkg.el
emacs --no-init-file --no-site-file --batch -L . -f batch-byte-compile *.el
emacs --no-init-file --no-site-file --batch \
    --eval '(setq generated-autoload-file "'$(pwd)'/51-tuareg-mode.el")' \
    -f batch-update-autoloads "."

%install
install -d %{buildroot}%{emacs_lispdir}/tuareg-mode
install -m 644 tuareg.el{c,} ocamldebug.el{c,} %{buildroot}%{emacs_lispdir}/tuareg-mode
install -d %{buildroot}%{emacs_startdir}
install -m 644 51-tuareg-mode.el %{buildroot}%{emacs_startdir}

%files
%doc README
%{emacs_lispdir}/tuareg-mode
%{emacs_startdir}/*.el

%changelog
* Sat Aug 24 2013 holgerar@gmail.com - 2.0.6-1
- Update to version 2.0.6
- The package now depends on the ocaml-emacs package.

* Sat Feb 11 2012 holgerar@gmail.com - 2.0.4-3
- Create package for version 2.0.4
