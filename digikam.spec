#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define tde_pkg digikam
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%if 0%{?mdkversion}
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		0.9.6
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Digital photo management application for TDE
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/graphics/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		digikam-open_in_digikam.desktop

BuildRequires:  cmake make
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-libkexiv2-devel
BuildRequires:	trinity-libkdcraw-devel
BuildRequires:	trinity-libkipi-devel

BuildRequires:	autoconf automake libtool m4
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
BuildRequires:	pkgconfig
BuildRequires:	libtool

# TIFF support
BuildRequires:  pkgconfig(libtiff-4)

BuildRequires:	gettext

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

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
%{tde_bindir}/digikam
%{tde_bindir}/digikamthemedesigner
%{tde_bindir}/digitaglinktree
%{tde_bindir}/showfoto
%{tde_libdir}/libdigikam.so.0
%{tde_libdir}/libdigikam.so.0.0.0
%{tde_tdelibdir}/tdeio_digikamalbums.la
%{tde_tdelibdir}/tdeio_digikamalbums.so
%{tde_tdelibdir}/tdeio_digikamdates.la
%{tde_tdelibdir}/tdeio_digikamdates.so
%{tde_tdelibdir}/digikamimageplugin_adjustcurves.la
%{tde_tdelibdir}/digikamimageplugin_adjustcurves.so
%{tde_tdelibdir}/digikamimageplugin_adjustlevels.la
%{tde_tdelibdir}/digikamimageplugin_adjustlevels.so
%{tde_tdelibdir}/digikamimageplugin_antivignetting.la
%{tde_tdelibdir}/digikamimageplugin_antivignetting.so
%{tde_tdelibdir}/digikamimageplugin_blurfx.la
%{tde_tdelibdir}/digikamimageplugin_blurfx.so
%{tde_tdelibdir}/digikamimageplugin_border.la
%{tde_tdelibdir}/digikamimageplugin_border.so
%{tde_tdelibdir}/digikamimageplugin_channelmixer.la
%{tde_tdelibdir}/digikamimageplugin_channelmixer.so
%{tde_tdelibdir}/digikamimageplugin_charcoal.la
%{tde_tdelibdir}/digikamimageplugin_charcoal.so
%{tde_tdelibdir}/digikamimageplugin_colorfx.la
%{tde_tdelibdir}/digikamimageplugin_colorfx.so
%{tde_tdelibdir}/digikamimageplugin_core.la
%{tde_tdelibdir}/digikamimageplugin_core.so
%{tde_tdelibdir}/digikamimageplugin_distortionfx.la
%{tde_tdelibdir}/digikamimageplugin_distortionfx.so
%{tde_tdelibdir}/digikamimageplugin_emboss.la
%{tde_tdelibdir}/digikamimageplugin_emboss.so
%{tde_tdelibdir}/digikamimageplugin_filmgrain.la
%{tde_tdelibdir}/digikamimageplugin_filmgrain.so
%{tde_tdelibdir}/digikamimageplugin_freerotation.la
%{tde_tdelibdir}/digikamimageplugin_freerotation.so
%{tde_tdelibdir}/digikamimageplugin_hotpixels.la
%{tde_tdelibdir}/digikamimageplugin_hotpixels.so
%{tde_tdelibdir}/digikamimageplugin_infrared.la
%{tde_tdelibdir}/digikamimageplugin_infrared.so
%{tde_tdelibdir}/digikamimageplugin_inpainting.la
%{tde_tdelibdir}/digikamimageplugin_inpainting.so
%{tde_tdelibdir}/digikamimageplugin_inserttext.la
%{tde_tdelibdir}/digikamimageplugin_inserttext.so
%{tde_tdelibdir}/digikamimageplugin_lensdistortion.la
%{tde_tdelibdir}/digikamimageplugin_lensdistortion.so
%{tde_tdelibdir}/digikamimageplugin_noisereduction.la
%{tde_tdelibdir}/digikamimageplugin_noisereduction.so
%{tde_tdelibdir}/digikamimageplugin_oilpaint.la
%{tde_tdelibdir}/digikamimageplugin_oilpaint.so
%{tde_tdelibdir}/digikamimageplugin_perspective.la
%{tde_tdelibdir}/digikamimageplugin_perspective.so
%{tde_tdelibdir}/digikamimageplugin_raindrop.la
%{tde_tdelibdir}/digikamimageplugin_raindrop.so
%{tde_tdelibdir}/digikamimageplugin_restoration.la
%{tde_tdelibdir}/digikamimageplugin_restoration.so
%{tde_tdelibdir}/digikamimageplugin_sheartool.la
%{tde_tdelibdir}/digikamimageplugin_sheartool.so
%{tde_tdelibdir}/digikamimageplugin_superimpose.la
%{tde_tdelibdir}/digikamimageplugin_superimpose.so
%{tde_tdelibdir}/digikamimageplugin_texture.la
%{tde_tdelibdir}/digikamimageplugin_texture.so
%{tde_tdelibdir}/digikamimageplugin_whitebalance.la
%{tde_tdelibdir}/digikamimageplugin_whitebalance.so
%{tde_tdelibdir}/tdeio_digikamsearch.la
%{tde_tdelibdir}/tdeio_digikamsearch.so
%{tde_tdelibdir}/tdeio_digikamtags.la
%{tde_tdelibdir}/tdeio_digikamtags.so
%{tde_tdelibdir}/tdeio_digikamthumbnail.la
%{tde_tdelibdir}/tdeio_digikamthumbnail.so
%{tde_tdeappdir}/digikam.desktop
%{tde_tdeappdir}/showfoto.desktop
%{tde_datadir}/apps/digikam/
%{tde_datadir}/apps/konqueror/servicemenus/digikam-download.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-gphoto2-camera.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-mount-and-download.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-open_in_digikam.desktop
%{tde_datadir}/apps/showfoto/
%{tde_datadir}/icons/hicolor/*/apps/digikam.png
%{tde_datadir}/icons/hicolor/*/apps/showfoto.png
%{tde_datadir}/services/digikamalbums.protocol
%{tde_datadir}/services/digikamdates.protocol
%{tde_datadir}/services/digikamimageplugin_adjustcurves.desktop
%{tde_datadir}/services/digikamimageplugin_adjustlevels.desktop
%{tde_datadir}/services/digikamimageplugin_antivignetting.desktop
%{tde_datadir}/services/digikamimageplugin_blurfx.desktop
%{tde_datadir}/services/digikamimageplugin_border.desktop
%{tde_datadir}/services/digikamimageplugin_channelmixer.desktop
%{tde_datadir}/services/digikamimageplugin_charcoal.desktop
%{tde_datadir}/services/digikamimageplugin_colorfx.desktop
%{tde_datadir}/services/digikamimageplugin_core.desktop
%{tde_datadir}/services/digikamimageplugin_distortionfx.desktop
%{tde_datadir}/services/digikamimageplugin_emboss.desktop
%{tde_datadir}/services/digikamimageplugin_filmgrain.desktop
%{tde_datadir}/services/digikamimageplugin_freerotation.desktop
%{tde_datadir}/services/digikamimageplugin_hotpixels.desktop
%{tde_datadir}/services/digikamimageplugin_infrared.desktop
%{tde_datadir}/services/digikamimageplugin_inpainting.desktop
%{tde_datadir}/services/digikamimageplugin_inserttext.desktop
%{tde_datadir}/services/digikamimageplugin_lensdistortion.desktop
%{tde_datadir}/services/digikamimageplugin_noisereduction.desktop
%{tde_datadir}/services/digikamimageplugin_oilpaint.desktop
%{tde_datadir}/services/digikamimageplugin_perspective.desktop
%{tde_datadir}/services/digikamimageplugin_raindrop.desktop
%{tde_datadir}/services/digikamimageplugin_restoration.desktop
%{tde_datadir}/services/digikamimageplugin_sheartool.desktop
%{tde_datadir}/services/digikamimageplugin_superimpose.desktop
%{tde_datadir}/services/digikamimageplugin_texture.desktop
%{tde_datadir}/services/digikamimageplugin_whitebalance.desktop
%{tde_datadir}/services/digikamsearch.protocol
%{tde_datadir}/services/digikamtags.protocol
%{tde_datadir}/services/digikamthumbnail.protocol
%{tde_datadir}/servicetypes/digikamimageplugin.desktop
%{tde_mandir}/man*/*
%{tde_tdedocdir}/HTML/en/digikam/
%{tde_tdedocdir}/HTML/en/showfoto/

##########

%package devel
Group:			Development/Libraries
Summary:		Development files for %{name}
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/digikam_export.h
%{tde_tdeincludedir}/digikam/
%{tde_libdir}/libdigikam.so
%{tde_libdir}/libdigikam.la

##########

%package i18n
Summary:		Translation files for %{tde_pkg}
Group:			Applications/Utilities
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description i18n
%{summary}

%files i18n
%defattr(-,root,root,-)
%lang(da) %{tde_tdedocdir}/HTML/da/digikam/
%lang(da) %{tde_tdedocdir}/HTML/da/showfoto/
%lang(de) %{tde_tdedocdir}/HTML/de/digikam/
%lang(de) %{tde_tdedocdir}/HTML/de/showfoto/
%lang(es) %{tde_tdedocdir}/HTML/es/digikam/
# %lang(es) %{tde_tdedocdir}/HTML/es/showfoto/
%lang(et) %{tde_tdedocdir}/HTML/et/digikam/
%lang(et) %{tde_tdedocdir}/HTML/et/showfoto/
%lang(it) %{tde_tdedocdir}/HTML/it/digikam/
%lang(it) %{tde_tdedocdir}/HTML/it/showfoto/
%lang(nl) %{tde_tdedocdir}/HTML/nl/digikam/
%lang(nl) %{tde_tdedocdir}/HTML/nl/showfoto/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/digikam/
%lang(ru) %{tde_tdedocdir}/HTML/ru/digikam/
%lang(sv) %{tde_tdedocdir}/HTML/sv/digikam/
%lang(sv) %{tde_tdedocdir}/HTML/sv/showfoto/

##########

%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}

# Hide 'showfoto'.
echo "NoDisplay=true" >> "$RPM_BUILD_ROOT%{tde_tdeappdir}/showfoto.desktop"

# Install the 'open in digikam' action for konqueror.
install -D -m 644 "%{SOURCE1}" "$RPM_BUILD_ROOT%{tde_datadir}/apps/konqueror/servicemenus/digikam-open_in_digikam.desktop"

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file digikam  Graphics Photography
%suse_update_desktop_file showfoto Graphics Viewer
%suse_update_desktop_file "$RPM_BUILD_ROOT%{tde_datadir}/apps/konqueror/servicemenus/digikam-open_in_digikam.desktop"
%endif

# Remove unwanted pixmaps
%__rm -rf %{?buildroot}%{tde_datadir}/pixmaps

