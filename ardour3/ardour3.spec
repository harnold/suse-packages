# Copyright 2014 Holger Arnold.
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

Name: ardour3
Summary: Digital audio workstation
Version: 3.5.380
Release: 1
License: GPL-2.0
Group: Productivity/Multimedia/Sound/Editors and Convertors
Url: http://ardour.org/
Requires: jack
Requires: lv2

Source: ardour-%{version}.tar.gz

BuildRequires: alsa-devel
BuildRequires: atkmm-devel
BuildRequires: boost-devel
BuildRequires: cairo-devel
BuildRequires: cairomm-devel
BuildRequires: fftw3-devel
BuildRequires: flac-devel
BuildRequires: glibmm2-devel
BuildRequires: gtk2-devel
BuildRequires: gtkmm2-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libaubio-devel
BuildRequires: libcurl-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libgnomecanvasmm-devel
BuildRequires: libjack-devel
BuildRequires: liblilv-0-devel
BuildRequires: liblo-devel >= 0.26
BuildRequires: liblrdf-devel
BuildRequires: libogg-devel
BuildRequires: libraptor-devel
BuildRequires: librasqal-devel
BuildRequires: libredland-devel
BuildRequires: librubberband-devel
BuildRequires: libsamplerate-devel
BuildRequires: libserd-0-devel
BuildRequires: libsigc++2-devel
BuildRequires: libsndfile-devel
BuildRequires: libsord-0-devel
BuildRequires: libsratom-0-devel
BuildRequires: libsuil-0-devel
BuildRequires: libtag-devel
BuildRequires: libuuid-devel
BuildRequires: libvamp-sdk2
BuildRequires: libvorbis-devel
BuildRequires: lv2-devel
BuildRequires: pangomm-devel
BuildRequires: python-rdflib

%description
Ardour is a professional digital workstation for working with audio and MIDI.

Ardour allows you to record and edit both audio and MIDI data, add many
different kinds of effects and mix.  Things you might use Ardour for include:
digitally record acoustic/electric instruments or vocals, compose and arrange
audio and MIDI tracks, edit live recordings, mix and edit movie soundtracks
and dialogue, create sound designs for an arbitrary number of output channels.

%prep
%setup -q -n ardour-%{version}

%build
export CFLAGS="%{optflags}"; \
export CXXFLAGS="%{optflags}"; \
./waf configure --prefix=%{_prefix} \
                --configdir=%{_sysconfdir} \
                --libdir=%{_libdir} \
                --optimize \
                --freedesktop \
                --no-phone-home \
                --noconfirm
./waf

%install
./waf install --destdir=%{buildroot}

for r in 16 22 32 48 256; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps
    install -m 644 \
        %{buildroot}%{_datadir}/ardour3/icons/ardour_icon_${r}px.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/ardour3.png
done

for r in 16 22 32 48; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/mimetypes
    install -m 644 \
        %{buildroot}%{_datadir}/ardour3/icons/application-x-ardour_${r}px.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/mimetypes/application-x-ardour3.png
done

install -d %{buildroot}%{_datadir}/applications
install -m 644 gtk2_ardour/ardour3.desktop.in \
    %{buildroot}%{_datadir}/applications/ardour3.desktop

install -d %{buildroot}%{_datadir}/mime/packages
install -m 644 gtk2_ardour/ardour3.xml %{buildroot}%{_datadir}/mime/packages/

gzip -9 ardour.1
install -d %{buildroot}%{_mandir}/man1
install -m 644 ardour.1.gz %{buildroot}%{_mandir}/man1/

%post
%desktop_database_post
%mime_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun

%files
%{_bindir}/*
%{_libdir}/ardour3
%{_libdir}/lv2/*
%{_datadir}/ardour3
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*
%{_datadir}/mime/packages/*
%{_mandir}/*/*
%config %{_sysconfdir}/ardour3
%doc COPYING README

%changelog
* Mon Aug 25 2014 holgerar@gmail.com - 3.5.380-1
- Create package for version 3.5.380.
