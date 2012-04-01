# Copyright 2011, 2012 Holger Arnold.
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
