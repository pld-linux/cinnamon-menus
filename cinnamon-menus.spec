#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	A menu system for the Cinnamon desktop
Summary(pl.UTF-8):	System menu dla środowiska Cinnamon
Name:		cinnamon-menus
Version:	6.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/linuxmint/cinnamon-menus/tags
Source0:	https://github.com/linuxmint/cinnamon-menus/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	69e64c8dcae0b13dc9db88876f390765
URL:		https://github.com/linuxmint/cinnamon
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gobject-introspection-devel >= 0.9.5
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	glib2 >= 1:2.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org.

%description -l pl.UTF-8
cinnamon-menus to implementacja szkicu "Desktop Menu Specification" z
freedesktop.org.

%package devel
Summary:	Header files for cinnamon-menu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cinnamon-menu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.30

%description devel
This package provides the necessary header files for writing
applications that use the Cinnamon menu system.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
wykorzystujących system menu Cinnamon.

%package apidocs
Summary:	API documentation for Cinnamon menu library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Cinnamon menu
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Cinnamon menu library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Cinnamon menu.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{!?debug:-Denable_debug=false} \
	%{?with_apidocs:-Denable_docs=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libcinnamon-menu-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcinnamon-menu-3.so.0
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcinnamon-menu-3.so
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir
%{_pkgconfigdir}/libcinnamon-menu-3.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cmenu
%endif
