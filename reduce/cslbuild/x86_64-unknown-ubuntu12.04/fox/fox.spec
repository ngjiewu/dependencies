%define name fox
%define version 1.6.21
%define release 1

Summary: The FOX toolkit.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: LGPL
Group: System Environment/Libraries
Source: ftp://ftp.fox-toolkit.org/pub/%{name}-%{version}.tar.gz
URL: http://www.fox-toolkit.org
Packager: Joshua Weage <joshua.weage@arup.com>
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
FOX is a C++-based library for graphical user interface development
FOX supports modern GUI features, such as drag-and-drop, tooltips, tab
books, tree lists, icons, multiple document interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics. Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package devel
Summary: Development files and documentation for the FOX GUI toolkit.
Group: Development/Libraries

%description devel
The fox-devel package contains the files necessary to develop applications
using the FOX GUI toolkit: the header files, the reswrap resource compiler,
manual pages, and HTML documentation.

%package static
Summary: A version of the FOX GUI toolkit for static linking.
Group: Development/Libraries

%description static
The fox-static package contains the files necessary to link applications
to the FOX GUI toolkit statically (rather than dynamically). Statically
linked applications do not require the library to be installed on the system
running the application.

%prep
%setup -q

%build
CPPFLAGS="$RPM_OPT_FLAGS -frtti" CFLAGS="$RPM_OPT_FLAGS -frtti" \
%configure --enable-release --enable-threadsafe
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f doc/Makefile.am doc/Makefile.in doc/Makefile
rm -r doc/art/Makefile.am doc/art/Makefile.in doc/art/Makefile
rm -f doc/screenshots/Makefile.am doc/screenshots/Makefile.in doc/screenshots/Makefile

# remove docs as they are supplied by rpm
rm -rf ${RPM_BUILD_ROOT}/%{_datadir}/doc/fox-1.6
rm -rf ${RPM_BUILD_ROOT}/usr/fox

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libFOX-1.6.so
%{_libdir}/libFOX-1.6.so.0
%{_libdir}/libFOX-1.6.so.0.0.21
%{_libdir}/libCHART-1.6.so
%{_libdir}/libCHART-1.6.so.0
%{_libdir}/libCHART-1.6.so.0.0.21

%doc doc
%doc ADDITIONS AUTHORS INSTALL LICENSE README TRACING index.html

%files devel
%defattr(-,root,root)
%{_bindir}/reswrap
%{_bindir}/fox-config
%{_mandir}/man1/reswrap.1*
%{_includedir}/fox-1.6
%{_libdir}/libFOX-1.6.la
%{_libdir}/libCHART-1.6.la
%{_libdir}/pkgconfig/fox.pc

%files static
%defattr(-,root,root)
%{_libdir}/libFOX-1.6.a
%{_libdir}/libCHART-1.6.a

%changelog
* Fri Aug 20 2004 Joshua Weage <joshua.weage@arup.com>
- Updated to use built-in RPM macros where possible.
- Sanity check RPM_BUILD_ROOT before deleting it.
- Delete docs installed by make, in preference for those from rpm

* Thu Dec 4 2003 Lyle Johnson <lyle@knology.net>
- incorporated Yan-Fa Li's changes for compatibility with latest RPM tools.

* Thu Sep 25 2003 Lyle Johnson <lyle@knology.net>
- added files for the new chart library to the fox, fox-devel and fox-static
  packages.
- added a Prefix tag to the header section so that this package is
  relocatable.
- Spin off Adie, calculator, PathFinder and shutterbug into their own subpackages.
- Removed the '--with-opengl=opengl' flag from the %build section (no longer needed).

* Thu Aug 28 2003 Lyle Johnson <lyle@users.sourceforge.net>
- correct installed file names to reflect new naming scheme

* Wed Aug 27 2002 Lyle Johnson <lyle@users.sourceforge.net>
- remove Makefile scraps from the doc subdirectories

* Wed Aug 21 2002 Lyle Johnson <lyle@users.sourceforge.net>
- added the fox-devel and fox-static subpackages.

* Tue Oct 10 2000 David Sugar <dyfet@ostel.com> 0.99.132-3
- rtti forced for rpm build specs that use -fno-rtti.

* Fri Mar 24 2000 Josi Romildo Malaquias <romildo@iceb.ufpo.b> 0.99.122-1
- new version

* Fri Mar 24 2000 Josi Romildo Malaquias <romildo@iceb.ufpo.b> 0.99.119-1
- new version

* Sun Mar 05 2000 Josi Romildo Malaquias <romildo@iceb.ufpo.b>
- some adaptations

* Tue Nov 10 1998 Reni van Paassen <M.M.vanPaassen@lr.tudelft.nl>
- initial package
