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
%global rocksdir %{_prefix}/local/lib/luarocks

Name:             luarocks
Summary:          Deployment and management system for Lua modules
Version:          2.0.8
Release:          1
License:          MIT
Group:            Development/Languages/Other
Url:              http://luarocks.org/
Source:           http://luarocks.org/releases/%{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    lua >= %{luaver}
BuildRequires:    lua-devel >= %{luaver}
BuildRequires:    luadoc
BuildRequires:    python-markdown
Requires:         lua >= %{luaver}
Requires:         wget

%description
LuaRocks allows you to install Lua modules as self-contained packages
called "rocks", which also contain version dependency information.
This information is used both during installation, so that when one
rock is requested all rocks it depends on are installed as well, and
at run time, so that when a module is required, the correct version is
loaded.  LuaRocks supports both local and remote repositories, and
multiple local rocks trees.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/luarocks \
    --lua-suffix=%{luaver} \
    --with-lua-include=%{_includedir} \
    --with-lua-lib=%{_libdir} \
    --rocks-tree=%{rocksdir} \
    --with-downloader=wget \
    --with-md5-checker=md5sum
make
markdown README.md > README.html

%install
%make_install

%post
install -d %{rocksdir}

%postun
[ "$(ls -A %{rocksdir})" ] || rmdir %{rocksdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/luarocks
%{_bindir}/*
%{lua_pkgdir}/luarocks
%doc COPYING README.html

%changelog
* Wed Feb 29 2012 holgerar@gmail.com - 2.0.8-1
- Update to version 2.0.8

* Sat Feb 11 2012 holgerar@gmail.com - 2.0.6-1
- Create package for version 2.0.6
