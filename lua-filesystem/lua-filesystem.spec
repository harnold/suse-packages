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

Name:             lua-filesystem
Summary:          File system library for the Lua programming language
Version:          1.5.0
Release:          2
License:          MIT
Group:            Development/Libraries/Other
Url:              http://www.keplerproject.org/luafilesystem/
Source:           http://github.com/downloads/keplerproject/luafilesystem/luafilesystem-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    lua >= %{luaver}
Requires:         lua >= %{luaver}

%description
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.  LuaFileSystem offers a portable way to access the
underlying directory structure and file attributes.

%prep
%setup -q -n luafilesystem-%{version}

%build
make \
    PREFIX=%{_prefix} \
    LUA_LIBDIR=%{lua_libdir} \
    CFLAGS="%{optflags}"

%install
make install \
    PREFIX=%{buildroot}%{_prefix} \
    LUA_LIBDIR=%{buildroot}%{lua_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{lua_libdir}/*
%doc README
%doc doc/us/*

%changelog
* Sat Feb 11 2012 holgerar@gmail.com - 1.5.0-1
- Create package for version 1.5.0
