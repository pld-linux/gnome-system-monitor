Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.24.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	edd7f02e30683054b94a89aa62c74d1e
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	glibmm-devel >= 2.16.2
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-icon-theme >= 2.22.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtkmm-devel
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libgtop-devel >= 1:2.23.4
BuildRequires:	librsvg-devel >= 2.22.0
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.22.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgtop >= 1:2.22.0
Requires:	libwnck >= 2.22.0
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
	--disable-scrollkeeper \
	--enable-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

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
