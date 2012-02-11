%global luaver 5.1
%global lua_libdir %{_libdir}/lua/%{luaver}
%global lua_pkgdir %{_datadir}/lua/%{luaver}

Name:             lua-logging
Summary:          A simple API to use logging features in Lua
Version:          1.1.4
Release:          1
Vendor:           http://harnold.org/
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
