Summary:	Simple process monitor
Summary(pl):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/2.0/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Buildrequires:	GConf2-devel >= 1.1.5
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	libwnck-devel >= 0.12
BuildRequires:	scrollkeeper
Obsoletes:	procman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define   _omf_dest_dir %(scrollkeeper-config --omfdir)

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

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name} --with-gnome

%post
/usr/bin/scrollkeeper-update
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

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
