Summary:	A menu system for the Cinnamon desktop
Summary(pl.UTF-8):	System menu dla środowiska Cinnamon
Name:		cinnamon-menus
Version:	3.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/linuxmint/cinnamon-menus/releases
Source0:	https://github.com/linuxmint/cinnamon-menus/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b38de2572887da7643bc2af7a509f592
URL:		http://cinnamon.linuxmint.com/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-introspection \
	--enable-debug%{!?debug:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcinnamon-menu-3.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcinnamon-menu-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcinnamon-menu-3.so.0
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcinnamon-menu-3.so
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir
%{_pkgconfigdir}/libcinnamon-menu-3.0.pc
