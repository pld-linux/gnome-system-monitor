Summary:	Simple process monitor
Summary(pl):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.8.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	3d4564b2d0b49a5826ae212b23d234df
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.8.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-vfs2-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libgnome-devel >= 2.8.0
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgtop-devel >= 1:2.8.0
BuildRequires:	libwnck-devel >= 2.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper
BuildRequires:	xft-devel >= 2.1-2
Requires(post):	GConf2
Requires(post):	scrollkeeper
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
cp /usr/share/gnome-common/data/omf.make .
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
