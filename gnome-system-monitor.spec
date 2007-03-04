Summary:	Simple process monitor
Summary(pl.UTF-8):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.17.95
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-system-monitor/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	e76c59b47578c8724abf1caae918758f
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.9
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-icon-theme >= 2.17.91
BuildRequires:	gnome-vfs2-devel >= 2.17.91
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
#BuildRequires:	libgksu-devel >= 1.3.8
BuildRequires:	libgtop-devel >= 1:2.14.8
BuildRequires:	libselinux-devel
BuildRequires:	libwnck-devel >= 2.17.92
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	libgtop >= 1:2.14.8
Requires:	libwnck >= 2.16.1
Obsoletes:	procman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl.UTF-8
Jest to prosty monitor procesów i systemu.

%prep
%setup -q
%patch0 -p1

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
%{_omf_dest_dir}/%{name}
