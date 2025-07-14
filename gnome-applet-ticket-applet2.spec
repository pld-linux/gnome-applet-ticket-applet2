Summary:	A GNOME2 applet for managing Kerberos tickets
Summary(pl.UTF-8):	Aplet GNOME2 do zarządzania biletami Kerberosa
Name:		gnome-applet-ticket-applet2
Version:	0.3
Release:	0.2
License:	GPL
Group:		X11/Applications
# some time ago at http://quackerhead.com/~duff/ticket_applet-2/download/ (no longer exists)
# now pulled from arch repo: http://mirrors.sourcecontrol.net/cduffy@spamcop.net--2003/ticket-applet--mainline
Source0:	ticket-applet--mainline--%{version}--patch-26.tar.bz2
# Source0-md5:	d606a5c6401c58d15f4b435f0ebf6f8f
Patch0:		%{name}-buildfix.patch
URL:		http://freshmeat.net/projects/ticket_applet-2/
BuildRequires:	GConf2-devel >= 2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.2
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	heimdal-devel
BuildRequires:	libcom_err-devel
BuildRequires:	libgnomeui-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Ticket Applet allows a user to view the amount of time remaining
on their Kerberos ticket or to grab a new ticket (optionally running
other programs -- ie. grabbing an AFS token).

%description -l pl.UTF-8
Ticket Applet umożliwia łatwe sprawdzenie ilości czasu przez jaką
ważny jest jeszcze bilet Kerberosa, pozwala także na łatwe pobranie
nowego biletu (opcjonalnie uruchamiając inne polecenia, tzn.
pobierając token AFS).

%prep
%setup -q -n ticket-applet--mainline--%{version}--patch-26
%patch -P0 -p1

%build
CFLAGS=-I/usr/include/et
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang ticket-applet-2-manual --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f ticket-applet-2-manual.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README TODO
%attr(755,root,root) %{_libexecdir}/ticket_applet-2
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_omf_dest_dir}/omf/*
%{_pixmapsdir}/*.png
