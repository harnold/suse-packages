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

Name:             lua-logging
Summary:          A simple API to use logging features in Lua
Version:          1.1.4
Release:          2
License:          MIT
Group:            Development/Libraries/Other
Url:              http://www.keplerproject.org/lualogging/
Source:           http://files.luaforge.net/releases/lualogging/lualogging/lualogging-%{version}/lualogging-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    lua >= %{luaver}
Requires:         lua >= %{luaver}

%description
LuaLogging provides a simple API to use logging features in Lua.  Its
design was based on log4j. LuaLogging currently supports, through the
use of appenders, console, file, email, socket and sql outputs.

%prep
%setup -q -n lualogging-%{version}

%build

%install
make install PREFIX=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{lua_pkgdir}/*
%doc README
%doc doc/us/*

%changelog
