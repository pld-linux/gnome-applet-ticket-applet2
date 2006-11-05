Summary:        A GNOME2 applet for managing Kerberos tickets
Summary(pl):    Applet GNOME2 do zarz±dzania biletami Kerberos'a
Name:           gnome-applet-krbticket
Version:        0.3
Release:        0.1
License:        GPL
Group:          X11/Applications
# some time ago at http://quackerhead.com/~duff/ticket_applet-2/download/ (no longer exists)
# now pulled from arch repo: http://mirrors.sourcecontrol.net/cduffy@spamcop.net--2003/ticket-applet--mainline
Source0:        ticket-applet--mainline--%{version}--patch-26.tar.bz2
# Source0-md5:	d606a5c6401c58d15f4b435f0ebf6f8f
Patch1:         %{name}-buildfix.patch
URL:		http://freshmeat.net/projects/ticket_applet-2/
BuildRequires:  gnome-panel-devel 
BuildRequires:  libcom_err-devel
BuildRequires:  heimdal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Ticket Applet allows a user to view the amount of time
remaining on their Kerberos ticket or to grab a new ticket
(optionally running other programs -- ie. grabbing an AFS
token).

%description -l pl
Ticket Applet umo¿liwia ³atwe sprawdzenie ilo¶ci czasu jaki 
wa¿ny jest jeszcze bilet Kerberos'a, pozwala tak¿e na ³atwe
pobranie nowego biletu (opcjonalnie uruchamiaj±c dowolne 
polecenie)

%prep
%setup -q -n ticket-applet--mainline--%{version}--patch-26
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/ticket_applet-2
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome/help/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/*
