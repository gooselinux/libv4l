Name:           libv4l
Version:        0.6.3
Release:        2%{?dist}
Summary:        Collection of video4linux support libraries 
Group:          System Environment/Libraries
# Some of the decompression helpers are GPLv2, the rest is LGPLv2+
License:        LGPLv2+ and GPLv2
URL:            http://hansdegoede.livejournal.com/3636.html
Source0:        http://people.fedoraproject.org/~jwrdegoede/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  kernel-headers

%description
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class. libv4l
consists of 3 different libraries: libv4lconvert, libv4l1 and libv4l2.

libv4lconvert offers functions to convert from any (known) pixelformat
to V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420.

libv4l1 offers the (deprecated) v4l1 API on top of v4l2 devices, independent
of the drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not).

libv4l2 offers the v4l2 API on top of v4l2 devices, while adding for the
application transparent libv4lconvert conversion where necessary.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" \
  PREFIX=%{_prefix} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING.LIB ChangeLog README TODO
%{_libdir}/libv4l*.so.*
%{_libdir}/libv4l

%files devel
%defattr(-,root,root,-)
%doc README.multi-threading
%{_includedir}/libv4l*.h
%{_libdir}/libv4l*.so
%{_libdir}/pkgconfig/libv4l*.pc


%changelog
* Wed Jan 27 2010 Hans de Goede <hdegoede@redhat.com> 0.6.3-2
- Fixup Source0 URL and License field.
  Related: rhbz#555835

* Sun Oct 25 2009 Hans de Goede <hdegoede@redhat.com> 0.6.3-1
- New upstream release 0.6.3

* Fri Oct  9 2009 Hans de Goede <hdegoede@redhat.com> 0.6.2-1
- New upstream release 0.6.2

* Tue Sep  1 2009 Hans de Goede <hdegoede@redhat.com> 0.6.1-1
- New upstream release 0.6.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Hans de Goede <hdegoede@redhat.com> 0.6.0-1
- New upstream release 0.6.0
- This fixes a divide by 0 crash in the whitebalancing code (#507748)

* Wed Jun  3 2009 Hans de Goede <hdegoede@redhat.com> 0.5.99-1
- New upstream release 0.5.99
- This fixes the crashes some people have been experiencing with 0.5.98
  (#503345)

* Tue May 26 2009 Hans de Goede <hdegoede@redhat.com> 0.5.98-1
- New upstream release 0.5.98

* Fri Mar 13 2009 Hans de Goede <hdegoede@redhat.com> 0.5.9-1
- New upstream release 0.5.9

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.8-1
- New upstream release 0.5.8

* Tue Dec  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.7-1
- New upstream release 0.5.7, fixing rh 473771

* Fri Nov 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.6-1
- New upstream release 0.5.6, working around rh 472468

* Thu Nov 20 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.5-1
- New upstream release 0.5.5, fixing rh 472217

* Mon Nov 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.4-1
- New upstream release 0.5.4

* Mon Oct 27 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.3-1
- New upstream release 0.5.3

* Thu Oct 23 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.2-1
- New upstream release 0.5.2

* Mon Oct 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.1-1
- New upstream release 0.5.1

* Mon Sep 15 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5.0-1
- New upstream release 0.5.0

* Fri Aug 29 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.2-1
- New upstream release 0.4.2

* Tue Aug 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.1-1
- New upstream release 0.4.1

* Sun Aug  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-1
- New upstream release 0.4.0

* Tue Jul 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.8-1
- New upstream release 0.3.8

* Sat Jul 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.7-1
- Initial Fedora package
