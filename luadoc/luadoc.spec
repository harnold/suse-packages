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