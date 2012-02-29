%global pkg magit

Name:             emacs-%{pkg}
Summary:          Emacs interface to Git
Version:          1.0.0
Release:          4
License:          GPLv3+, GFDLv1.2+
Group:            Productivity/Editors/Emacs
Url:              http://philjackson.github.com/magit/
Source:           http://github.com/downloads/magit/magit/%{pkg}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
BuildArch:        noarch
BuildRequires:    emacs
BuildRequires:    texinfo
BuildRequires:    python-markdown
Requires(post):   info
Requires(preun):  info
Requires:         emacs
Requires:         git-core

%description
Magit is an Emacs interface to the Git version control system.
It provides convenient access to the most common Git operations.

%global emacs_lispdir  %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d

%prep
%setup -q -n %{pkg}-%{version}

%build
emacs --no-init-file --no-site-file --batch \
      --eval "(push (expand-file-name \".\") load-path)" \
      -f batch-byte-compile *.el
makeinfo magit.texi
gzip magit.info
makeinfo --html --no-split magit.texi
markdown README.md > README.html

%install
install -d %{buildroot}%{emacs_lispdir}/%{pkg}
install -m 644 magit*.el{c,} %{buildroot}%{emacs_lispdir}/%{pkg}
install -d %{buildroot}%{emacs_startdir}
install -m 644 50magit.el %{buildroot}%{emacs_startdir}/init-%{pkg}.el
install -d %{buildroot}%{_infodir}
install -m 644 magit.info.gz %{buildroot}%{_infodir}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/magit.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/magit.info.gz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.html magit.html
%doc %{_infodir}/magit.info.gz
%{emacs_startdir}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/*.el

%changelog
