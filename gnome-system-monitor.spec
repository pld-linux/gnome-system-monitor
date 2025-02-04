#
# Conditional build:
%bcond_without	systemd	# systemd support
#
Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	47.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-system-monitor/47/%{name}-%{version}.tar.xz
# Source0-md5:	f6e69d246adc5445228c82011fac118a
Patch0:		%{name}-no-update.patch
URL:		https://apps.gnome.org/SystemMonitor/
BuildRequires:	atkmm-devel >= 2.28
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
# -std=c2x
BuildRequires:	gcc >= 6:11
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	glibmm2.68-devel >= 2.68
BuildRequires:	gtk4-devel >= 4.12.0
BuildRequires:	gtkmm4-devel >= 4.0.0
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	libgtop-devel >= 1:2.41.2
BuildRequires:	librsvg-devel >= 2.46
# -std=gnu++20
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxml2-progs
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
%{?with_systemd:BuildRequires:	systemd-devel >= 44}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.56.0
Requires:	atkmm >= 2.28
Requires:	glib2 >= 1:2.56.0
Requires:	glibmm2.68 >= 2.68
Requires:	gtk4 >= 4.12.0
Requires:	gtkmm4 >= 4.0.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.6
Requires:	libgtop >= 1:2.41.2
Requires:	librsvg >= 2.46
Obsoletes:	procman < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl.UTF-8
GNOME System Monitor to prosty monitor procesów i systemu.

%prep
%setup -q
%patch -P0 -p1

%build
%meson build \
	%{!?with_systemd:-Dsystemd=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%dir %{_libexecdir}/gnome-system-monitor
%attr(755,root,root) %{_libexecdir}/gnome-system-monitor/gsm-kill
%attr(755,root,root) %{_libexecdir}/gnome-system-monitor/gsm-renice
%attr(755,root,root) %{_libexecdir}/gnome-system-monitor/gsm-taskset
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/gnome-system-monitor
%{_datadir}/metainfo/org.gnome.SystemMonitor.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
%{_desktopdir}/gnome-system-monitor-kde.desktop
%{_desktopdir}/org.gnome.SystemMonitor.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.SystemMonitor.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.SystemMonitor.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SystemMonitor-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/processes-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/resources-symbolic.svg
