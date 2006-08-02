Summary:	Simple process monitor
Summary(pl):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.14.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-system-monitor/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	1220837542f9c1905ebf3af69a608b07
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.9.1
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-vfs2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libgksu-devel >= 0.15.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libgtop-devel >= 1:2.14.0
BuildRequires:	libselinux-devel
BuildRequires:	libwnck-devel >= 2.14.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	xft-devel >= 2.1-2
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	libgnomeui >= 2.14.0
Requires:	libgtop >= 1:2.14.0
Requires:	libwnck >= 2.14.1
Obsoletes:	procman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl
Jest to prosty monitor procesów i systemu.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
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
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/gnome-system-monitor.schemas
%{_omf_dest_dir}/%{name}
