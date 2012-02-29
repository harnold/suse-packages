Name:             emacs
Summary:          The GNU Emacs text editor
Version:          24.0.94
Release:          1
License:          GPLv3+
Group:            Productivity/Editors/Emacs
Url:              http://www.gnu.org/software/emacs/
# Source0:          http://ftp.gnu.org/pub/gnu/emacs/emacs-%{version}.tar.gz
Source0:          http://alpha.gnu.org/gnu/emacs/pretest/emacs-%{version}.tar.gz
Source1:          site-start.el
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildRequires:    texinfo
BuildRequires:    xorg-x11-devel
BuildRequires:    gtk3-devel
BuildRequires:    freetype2-devel
BuildRequires:    gconf2-devel
BuildRequires:    dbus-1-devel
BuildRequires:    libxml2-devel
BuildRequires:    libpng14-devel
BuildRequires:    libjpeg62-devel
BuildRequires:    libtiff-devel
BuildRequires:    giflib-devel
BuildRequires:    librsvg-devel
BuildRequires:    ImageMagick-devel
BuildRequires:    zlib-devel
BuildRequires:    m17n-lib-devel
BuildRequires:    libotf-devel
BuildRequires:    libgnutls-devel
BuildRequires:    gpm-devel
BuildRequires:    alsa-devel
Requires(post):   info
Requires(preun):  info
Provides:         emacs_program = %{version}-%{release}

%description
GNU Emacs is an extensible, customizable text editor—and more.

%package el
Summary:          Emacs Lisp sources
BuildArch:        noarch
Requires:         emacs = %{version}-%{release}

%description el
This package contains the Lisp source files of Emacs.  You do not need
these files to run Emacs.

%global info_files ada-mode auth autotype calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eieio eintr elisp emacs emacs-mime epa erc ert eshell eudc flymake forms gnus idlwave info mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar tramp url viper vip widget woman

%global site_lisp_dir  %{_datadir}/emacs/site-lisp
%global site_start_dir %{site_lisp_dir}/site-start.d

%prep
%setup -q -T -b 0

%build
%configure \
    --docdir=%{_defaultdocdir} \
    --with-x-toolkit=gtk3
make %{?_smp_mflags}

%install
%make_install
install -m 644 %{SOURCE1} %{buildroot}%{site_lisp_dir}
install -d %{buildroot}%{site_start_dir}
rm %{buildroot}%{_infodir}/dir
rm %{buildroot}%{_bindir}/ctags
rm %{buildroot}%{_bindir}/emacs-%{version}

rm -f emacs-files emacs-el-files
(
    build_dir=$(pwd)
    cd %{buildroot}

    find .%{_datadir}/emacs \
        \( -type f -name "*.el.gz" -fprint "$build_dir"/emacs-el-filelist \) -o \
        \( -type f -fprint "$build_dir"/emacs-files \) -o \
        \( -type d -fprintf "$build_dir"/emacs-dirs "%%%%dir %%h/%%f\n" \)

)
cat emacs-dirs emacs-files > emacs-filelist
sed -i -e "s|\.%{_prefix}|%{_prefix}|" emacs-filelist emacs-el-filelist

%post
for f in %{info_files}; do
    %install_info --info-dir=%{_infodir} %{_infodir}/$f.gz
done
%desktop_database_post
%icon_theme_cache_post

%postun
for f in %{info_files}; do
    %install_info_delete --info-dir=%{_infodir} %{_infodir}/$f.gz
done
%desktop_database_postun
%icon_theme_cache_postun

%clean
rm -rf %{buildroot}

%files -f emacs-filelist
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/emacs
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_localstatedir}/games/emacs
%doc %{_infodir}/*
%doc %{_mandir}/*/*
%doc BUGS COPYING README

%files -f emacs-el-filelist el
%defattr(-,root,root)

%changelog
