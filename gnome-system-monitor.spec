Summary:	Simple process monitor
Summary(pl):	Prosty monitor procesów
Name:		gnome-system-monitor
Version:	2.7.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	e2e46c3ee26458a808d52071b7420413
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.3.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libgnome-devel >= 2.7.1
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libgtop-devel >= 1:2.7.92
BuildRequires:	libwnck-devel >= 2.6.2
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
%patch1 -p1

mv po/{no,nb}.po

%build
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
