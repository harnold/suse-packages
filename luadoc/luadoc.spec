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

%global luaver 5.1
%global lua_libdir %{_libdir}/lua/%{luaver}
%global lua_pkgdir %{_datadir}/lua/%{luaver}

Name:             luadoc
Summary:          Documentation generator for Lua
Version:          3.0.1
Release:          2
License:          MIT
Group:            Development/Languages/Other
Url:              http://keplerproject.github.com/luadoc/
Source:           http://files.luaforge.net/releases/luadoc/luadoc/LuaDoc-%{version}/%{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    lua >= %{luaver}
Requires:         lua >= %{luaver}
Requires:         lua-filesystem
Requires:         lua-logging

%description
LuaDoc is a documentation generator tool for Lua source code.  It
parses the declarations and documentation comments in a set of Lua
source files and produces a set of XHTML pages describing the
commented declarations and functions.

The output is not limited to XHTML. Other formats can be generated by
implementing new doclets. The format of the documentation comments is
also flexible and can be customized by implementing new taglets.
Please refer to customizing section for further information.

%prep
%setup -q

%build

%install
make install \
    PREFIX=%{buildroot}%{_prefix} \
    LUA_LIBDIR=%{buildroot}%{lus_libdir} \
    LUA_DIR=%{buildroot}%{lua_pkgdir} \
    SYS_BINDIR=%{buildroot}%{_bindir} \
    LUA_INTERPRETER=%{_bindir}/lua%{luaver}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{lua_pkgdir}/luadoc
%doc README
%doc doc/us/*

%changelog
