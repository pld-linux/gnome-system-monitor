Summary:	Simple process monitor
Summary(pl):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.3.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	3d54999127ccfc39f4e7f8e73080b5f3
URL:		http://www.gnome.org/
Buildrequires:	GConf2-devel >= 2.1.90
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libgnome-devel >= 2.1.90
BuildRequires:	libgnomeui-devel >= 2.1.90
BuildRequires:	libgtop-devel >= 2.0.1
BuildRequires:	libwnck-devel >= 2.1.90
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper
BuildRequires:	Xft-devel >= 2.1-2
Obsoletes:	procman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple process and system monitor.

%description -l pl
Jest to prosty monitor procesów i systemu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-system-monitor
%{_datadir}/applications/*
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
