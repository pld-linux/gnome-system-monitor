Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.26.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	d69ddb569e51ba381b6bf2d8d32f3b78
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glibmm-devel >= 2.16.2
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 2.24.0
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.24.0
BuildRequires:	librsvg-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.24.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgtop >= 1:2.24.0
Requires:	libwnck >= 2.24.0
Obsoletes:	procman
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl.UTF-8
Jest to prosty monitor procesów i systemu.

%prep
%setup -q

%build
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-system-monitor.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gnome-system-monitor.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%{_desktopdir}/gnome-system-monitor.desktop
%{_pixmapsdir}/gnome-system-monitor
%{_sysconfdir}/gconf/schemas/gnome-system-monitor.schemas
