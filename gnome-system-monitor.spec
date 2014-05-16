# Conditional build:
%bcond_without	systemd		# systemd support
#
Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	3.12.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	dc9f4ffa25ebee2795821251ef0d73db
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	glibmm-devel >= 2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.20.0
BuildRequires:	gnome-icon-theme >= 3.0.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtkmm3-devel >= 3.4.0
BuildRequires:	intltool >= 0.41.0
BuildRequires:	libgtop-devel >= 1:2.28.2
BuildRequires:	librsvg-devel >= 2.35.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwnck-devel >= 3.0.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
%{?with_systemd:BuildRequires:	systemd-devel >= 43}
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gnome-icon-theme >= 3.0.0
Requires:	libgtop >= 1:2.28.2
Obsoletes:	procman
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl.UTF-8
GNOME System Monitor to prosty monitor procesów i systemu.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable systemd systemd} \
	--disable-silent-rules \
	--disable-schemas-compile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%dir %{_libdir}/gnome-system-monitor
%attr(755,root,root) %{_libdir}/gnome-system-monitor/gsm-kill
%attr(755,root,root) %{_libdir}/gnome-system-monitor/gsm-renice
%{_datadir}/appdata/gnome-system-monitor.appdata.xml
%{_desktopdir}/gnome-system-monitor.desktop
%{_desktopdir}/gnome-system-monitor-kde.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
