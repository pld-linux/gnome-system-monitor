Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.20.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	52d02162cecd0174536148197024126d
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-icon-theme >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtkmm-devel
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libgtop-devel >= 1:2.20.0
BuildRequires:	libselinux-devel
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgtop >= 1:2.20.0
Requires:	libwnck >= 2.20.0
Obsoletes:	procman
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
%{__aclocal}
%{__autoconf}
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

%find_lang %{name} --with-gnome

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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gnome-system-monitor
%{_sysconfdir}/gconf/schemas/gnome-system-monitor.schemas
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-C.omf
%lang(bg) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-bg.omf
%lang(ca) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-ca.omf
%lang(es) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-fr.omf
%lang(oc) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-oc.omf
%lang(pa) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-pa.omf
%lang(sv) %{_omf_dest_dir}/gnome-system-monitor/gnome-system-monitor-sv.omf
