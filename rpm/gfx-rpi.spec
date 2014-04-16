%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

Name:       gfx-rpi


Summary:    VideoCore libraries for Raspberry Pi
Version:    0.0.4
Release:    1
Group:      Graphics/Display and Graphics Adaptation
License:    Broadcom Proprietary
URL:        https://github.com/raspberrypi/firmware
Source0:    gfx-rpi-%{version}.tar.xz
Source1:    egl.pc
Source2:    glesv1_cm.pc
Source3:    glesv2.pc
Source4:    omxil.pc
Source5:    bcm_host.pc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Broadcom VideoCore Linux libraries for Raspberry Pi
This package contains the common binaries and libraries.

%package devel
Summary:    Common devel files for RaspberryPi Broadcom VideoCore
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
Headers for common RaspberryPi Broadcom VideoCore.

%package libOMXIL
Summary:    OMX IL for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libOMXIL = %{version}-%{release}
Provides:   libopenmaxil.so

%description libOMXIL
This package provides OMX IL library for Broadcom VideoCore


%package libOMXIL-devel
Summary:    OMX IL development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libEGL = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Provides:   libOMXIL-devel

%description libOMXIL-devel
This package provides OMXIL headers for Broadcom VideoCore.

%package libEGL
Summary:    EGL for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}
Provides:   libEGL.so.1

%description libEGL
This package provides EGL library for Broadcom VideoCore


%package libEGL-devel
Summary:    EGL development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libEGL = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Provides:   libEGL-devel

%description libEGL-devel
This package provides EGL headers for Broadcom VideoCore.


%package libGLESv1
Summary:    GLESv1 for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}
Provides:   libGLES_CM.so.1

%description libGLESv1
This package provides OpenGL ES v1 libraries for Broadcom VideoCore.


%package libGLESv1-devel
Summary:    GLESv1 development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libGLESv1 = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
This package provides OpenGL ES v1 headers for Broadcom VideoCore.


%package libGLESv2
Summary:    GLESv2 for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}
Provides:   libGLESv2.so.2

%description libGLESv2
This package provides OpenGL ES v2 libraries for Broadcom VideoCore.


%package libGLESv2-devel
Summary:    GLESv2 development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libGLESv2 = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Provides:   libGLESv2-devel

%description libGLESv2-devel
This package provides OpenGL ES v2 headers for Broadcom VideoCore.



%prep
%setup -q -n %{name}-%{version}/upstream

%build




%install
rm -rf %{buildroot}

install -d %{buildroot}/
mkdir -p %{buildroot}/usr
%ifarch armv6hl
rm -rf hardfp/opt/vc/src
cp -av hardfp/opt/vc/* %{buildroot}/usr/
%else
rm -rf opt/vc/src
cp -av opt/vc/* %{buildroot}/usr/
%endif
chmod 0755 %{buildroot}/%{_bindir}/*
chmod 0755 %{buildroot}/%{_sbindir}/*
chmod 0755 %{buildroot}/%{_libdir}/*so
# Set all files 0644 (don't touch directories)
find %{buildroot}/%{_includedir}/ -type f -exec chmod 0644 {} \;
ln -s libEGL.so %{buildroot}/%{_libdir}/libEGL.so.1
ln -s libGLESv2.so %{buildroot}/%{_libdir}/libGLESv2.so.2
ln -s  %{buildroot}/%{_libdir}/

mkdir -p %{buildroot}/%{_docdir}/
mv %{buildroot}/usr/LICENCE %{buildroot}/%{_docdir}/LICENCE
mkdir -p %{buildroot}/usr/lib/pkgconfig
cp %{SOURCE1} %{buildroot}/usr/lib/pkgconfig/
cp %{SOURCE2} %{buildroot}/usr/lib/pkgconfig/
cp %{SOURCE3} %{buildroot}/usr/lib/pkgconfig/
cp %{SOURCE4} %{buildroot}/usr/lib/pkgconfig/
cp %{SOURCE5} %{buildroot}/usr/lib/pkgconfig/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post libOMXIL -p /sbin/ldconfig

%postun libOMXIL -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_bindir}/vcdbg
%{_bindir}/vcgencmd
%{_bindir}/edidparser
%{_bindir}/vchiq_test
%{_bindir}/tvservice
%{_bindir}/raspistill
%{_bindir}/raspivid
%{_bindir}/raspiyuv
%{_sbindir}/vcfiled
%{_bindir}/mmal_vc_diag
%{_libdir}/libmmal.so
%{_libdir}/libmmal_core.so
%{_libdir}/libmmal_util.so
%{_libdir}/libmmal_vc_client.so
%{_libdir}/libWFC.so
%{_libdir}/libOpenVG.so
%{_libdir}/libvcos.so
%{_libdir}/libvchiq_arm.so
%{_libdir}/libdebug_sym.so
%{_libdir}/libbcm_host.so


%files devel
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_includedir}/interface
%{_includedir}/vcinclude
%{_includedir}/VG
%{_includedir}/WF
%{_includedir}/bcm_host.h
%{_libdir}/libvchostif.a
%{_libdir}/libvcfiled_check.a
%{_libdir}/libvmcs_rpc_client.a


%files libOMXIL
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_libdir}/libopenmaxil.so

%files libOMXIL-devel
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_includedir}/IL/*.h
%{_libdir}/pkgconfig/omxil.pc

%files libEGL
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_libdir}/libEGL.so*

%files libEGL-devel
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_includedir}/KHR/*.h
%{_includedir}/EGL/*.h
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/bcm_host.pc
%{_libdir}/libEGL_static.a
%{_libdir}/libkhrn_client.a
%{_libdir}/libkhrn_static.a


%files libGLESv1
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_libdir}/libGLESv1_CM.so*

%files libGLESv1-devel
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_includedir}/GLES/*.h
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_libdir}/libGLESv2.so*

%files libGLESv2-devel
%defattr(-,root,root,-)

%doc %{_docdir}/LICENCE
%{_includedir}/GLES2/*.h
%{_libdir}/pkgconfig/glesv2.pc
%{_libdir}/libGLESv2_static.a
