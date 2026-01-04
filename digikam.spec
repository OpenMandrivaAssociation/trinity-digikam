%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg digikam
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		0.9.6
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Digital photo management application for TDE
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/graphics/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		digikam-open_in_digikam.desktop

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-libkexiv2-devel
BuildRequires:	trinity-libkdcraw-devel
BuildRequires:	trinity-libkipi-devel

# BuildRequires:	autoconf automake libtool m4

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# TIFF support
BuildRequires:  pkgconfig(libtiff-4)

BuildRequires:	gettext

# LCMS support
BuildRequires:  pkgconfig(lcms)

# GPHOTO2 support
BuildRequires:  pkgconfig(libgphoto2)

# JASPER support
BuildRequires:  pkgconfig(jasper)

# EXIV2 support
BuildRequires:  pkgconfig(exiv2)

# SQLITE support
BuildRequires:  pkgconfig(sqlite3)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)

Requires:		trinity-libkexiv2
Requires:		trinity-libkipi
Requires:		trinity-libkdcraw

%description
An easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating
digital photos a "snap".  An interface is provided to connect to
your digital camera, preview the images and download and/or
delete them.

The digiKam built-in image editor makes the common photo correction
a simple task. The image editor is extensible via plugins and,
the digikamimageplugins project has been merged to digiKam core
since release 0.9.2, all useful image editor plugins are available
in the base installation.

digiKam can also make use of the KIPI image handling plugins to
extend its capabilities even further for photo manipulations,
import and export, etc. The kipi-plugins package contains many
very useful extentions.

digiKam is based in part on the work of the Independent JPEG Group.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/bin/digikam
%{tde_prefix}/bin/digikamthemedesigner
%{tde_prefix}/bin/digitaglinktree
%{tde_prefix}/bin/showfoto
%{tde_prefix}/%{_lib}/libdigikam.so.0
%{tde_prefix}/%{_lib}/libdigikam.so.0.0.0
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamalbums.la
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamalbums.so
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamdates.la
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamdates.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_adjustcurves.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_adjustcurves.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_adjustlevels.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_adjustlevels.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_antivignetting.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_antivignetting.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_blurfx.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_blurfx.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_border.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_border.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_channelmixer.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_channelmixer.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_charcoal.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_charcoal.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_colorfx.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_colorfx.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_core.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_core.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_distortionfx.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_distortionfx.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_emboss.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_emboss.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_filmgrain.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_filmgrain.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_freerotation.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_freerotation.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_hotpixels.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_hotpixels.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_infrared.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_infrared.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_inpainting.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_inpainting.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_inserttext.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_inserttext.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_lensdistortion.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_lensdistortion.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_noisereduction.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_noisereduction.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_oilpaint.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_oilpaint.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_perspective.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_perspective.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_raindrop.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_raindrop.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_restoration.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_restoration.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_sheartool.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_sheartool.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_superimpose.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_superimpose.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_texture.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_texture.so
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_whitebalance.la
%{tde_prefix}/%{_lib}/trinity/digikamimageplugin_whitebalance.so
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamsearch.la
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamsearch.so
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamtags.la
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamtags.so
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamthumbnail.la
%{tde_prefix}/%{_lib}/trinity/tdeio_digikamthumbnail.so
%{tde_prefix}/share/applications/tde/digikam.desktop
%{tde_prefix}/share/applications/tde/showfoto.desktop
%{tde_prefix}/share/apps/digikam/
%{tde_prefix}/share/apps/konqueror/servicemenus/digikam-download.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/digikam-gphoto2-camera.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/digikam-mount-and-download.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/digikam-open_in_digikam.desktop
%{tde_prefix}/share/apps/showfoto/
%{tde_prefix}/share/icons/hicolor/*/apps/digikam.png
%{tde_prefix}/share/icons/hicolor/*/apps/showfoto.png
%{tde_prefix}/share/services/digikamalbums.protocol
%{tde_prefix}/share/services/digikamdates.protocol
%{tde_prefix}/share/services/digikamimageplugin_adjustcurves.desktop
%{tde_prefix}/share/services/digikamimageplugin_adjustlevels.desktop
%{tde_prefix}/share/services/digikamimageplugin_antivignetting.desktop
%{tde_prefix}/share/services/digikamimageplugin_blurfx.desktop
%{tde_prefix}/share/services/digikamimageplugin_border.desktop
%{tde_prefix}/share/services/digikamimageplugin_channelmixer.desktop
%{tde_prefix}/share/services/digikamimageplugin_charcoal.desktop
%{tde_prefix}/share/services/digikamimageplugin_colorfx.desktop
%{tde_prefix}/share/services/digikamimageplugin_core.desktop
%{tde_prefix}/share/services/digikamimageplugin_distortionfx.desktop
%{tde_prefix}/share/services/digikamimageplugin_emboss.desktop
%{tde_prefix}/share/services/digikamimageplugin_filmgrain.desktop
%{tde_prefix}/share/services/digikamimageplugin_freerotation.desktop
%{tde_prefix}/share/services/digikamimageplugin_hotpixels.desktop
%{tde_prefix}/share/services/digikamimageplugin_infrared.desktop
%{tde_prefix}/share/services/digikamimageplugin_inpainting.desktop
%{tde_prefix}/share/services/digikamimageplugin_inserttext.desktop
%{tde_prefix}/share/services/digikamimageplugin_lensdistortion.desktop
%{tde_prefix}/share/services/digikamimageplugin_noisereduction.desktop
%{tde_prefix}/share/services/digikamimageplugin_oilpaint.desktop
%{tde_prefix}/share/services/digikamimageplugin_perspective.desktop
%{tde_prefix}/share/services/digikamimageplugin_raindrop.desktop
%{tde_prefix}/share/services/digikamimageplugin_restoration.desktop
%{tde_prefix}/share/services/digikamimageplugin_sheartool.desktop
%{tde_prefix}/share/services/digikamimageplugin_superimpose.desktop
%{tde_prefix}/share/services/digikamimageplugin_texture.desktop
%{tde_prefix}/share/services/digikamimageplugin_whitebalance.desktop
%{tde_prefix}/share/services/digikamsearch.protocol
%{tde_prefix}/share/services/digikamtags.protocol
%{tde_prefix}/share/services/digikamthumbnail.protocol
%{tde_prefix}/share/servicetypes/digikamimageplugin.desktop
%{tde_prefix}/share/man/man*/*
%{tde_prefix}/share/doc/tde/HTML/en/digikam/
%{tde_prefix}/share/doc/tde/HTML/en/showfoto/

##########

%package devel
Group:			Development/Libraries
Summary:		Development files for %{name}
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/digikam_export.h
%{tde_prefix}/include/tde/digikam/
%{tde_prefix}/%{_lib}/libdigikam.so
%{tde_prefix}/%{_lib}/libdigikam.la

##########

%package i18n
Summary:		Translation files for %{tde_pkg}
Group:			Applications/Utilities
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description i18n
%{summary}

%files i18n
%defattr(-,root,root,-)
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/digikam/
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/showfoto/
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/digikam/
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/showfoto/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/digikam/
# %lang(es) %{tde_prefix}/share/doc/tde/HTML/es/showfoto/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/digikam/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/showfoto/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/digikam/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/showfoto/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/digikam/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/showfoto/
%lang(pt_BR) %{tde_prefix}/share/doc/tde/HTML/pt_BR/digikam/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/digikam/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/digikam/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/showfoto/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Hide 'showfoto'.
echo "NoDisplay=true" >> "$RPM_BUILD_ROOT%{tde_prefix}/share/applications/tde/showfoto.desktop"

# Install the 'open in digikam' action for konqueror.
install -D -m 644 "%{SOURCE1}" "$RPM_BUILD_ROOT%{tde_prefix}/share/apps/konqueror/servicemenus/digikam-open_in_digikam.desktop"

# Remove unwanted pixmaps
%__rm -rf %{?buildroot}%{tde_prefix}/share/pixmaps

