#
# Conditional build:
%bcond_with	debug		# enable debugging

Summary:	A menu system for the Cinnamon project
Name:		cinnamon-menus
Version:	2.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/linuxmint/cinnamon-menus/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	55bb91d9882c8c5d9972fbdc444a4c9f
URL:		http://cinnamon.linuxmint.com/
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains the
Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a simple
menu editor.

%package devel
Summary:	Libraries and include files for the Cinnamon menu system
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for writing
applications that use the Cinnamon menu system.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-introspection \
	--enable-debug=%{!?with_debug:no}%{?with_debug:yes}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcinnamon-menu-3.la

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS COPYING.LIB
%{_libdir}/libcinnamon-menu-3.so.*.*.*
%ghost %{_libdir}/libcinnamon-menu-3.so.0
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcinnamon-menu-3.so
%{_pkgconfigdir}/libcinnamon-menu-3.0.pc
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir
