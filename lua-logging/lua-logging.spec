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

Name:             lua-logging
Summary:          A simple API to use logging features in Lua
Version:          1.1.4
Release:          3
License:          MIT
Group:            Development/Libraries/Other
Url:              http://www.keplerproject.org/lualogging/
Source:           http://files.luaforge.net/releases/lualogging/lualogging/lualogging-%{version}/lualogging-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    lua-devel >= %{luaver}
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
* Thu Nov 15 2012 holgerar@gmail.com - 1.1.4-3
- Add build dependency on lua-devel >= 5.1

* Sat Feb 11 2012 holgerar@gmail.com - 1.1.4-1
- Create package for version 1.1.4
