Summary:	Simple process monitor
Summary(pl):	Prosty monitor proces�w
Name:		gnome-system-monitor
Version:	2.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	627167b4395f119d0c8439ec83518edb
Patch0:		%{name}-gtksnap.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.3.0-1.20031126.1
BuildRequires:	libgnome-devel >= 2.5.0
BuildRequires:	libgnomeui-devel >= 2.5.0
BuildRequires:	libgtop-devel >= 2.5.0
BuildRequires:	libwnck-devel >= 2.5.0
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
Jest to prosty monitor proces�w i systemu.

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
