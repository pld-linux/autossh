Summary:	Automatically restart SSH sessions and tunnels
Summary(pl):	Automatyczny restart sesji i tuneli SSH
Name:		autossh
Version:	1.2b
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		Carson Harding <carson.harding@shaw.ca>
Source0:	http://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
URL:		http://www.harding.motd.ca/autossh/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic. The idea and
the mechanism are from rstunnel (Reliable SSH Tunnel), but implemented
in C. The author's view is that it is not as fiddly as rstunnel to get
to work. Connection monitoring using a loop of port forwardings. Backs
off on rate of connection attempts when experiencing rapid failures
such as connection refused. Compiled and tested on OpenBSD, Linux, and
Solaris; should work fine on other BSDs (except Mac OS 10).

%prep
%setup -q -n %{name}-%{version}

%build
%{__make} -f Makefile.linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install autossh $RPM_BUILD_ROOT%{_bindir}
install autossh.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES autossh.host rscreen
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
