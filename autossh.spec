Summary:	Automatically restart SSH sessions and tunnels
Summary(pl):	Automatyczny restart sesji i tuneli SSH
Name:		autossh
Version:	1.2g
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		Carson Harding <carson.harding@shaw.ca>
Source0:	http://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
# Source0-md5:	2422e7dbcc21a48dfc325ceb974c9345
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

%description -l pl
autossh jest programem uruchamiaj±cym kopiê ssh i monitoruj±cym j±,
restartuj±c w miarê potrzeby, je¶li umrze lub przestanie przekazywaæ
ruch. Idea i mechanizm pochodz± z rstunnela (Reliable SSH Tunnel), ale
zaimplementowano je w C. Wed³ug autora nie trzeba siê tak patyczkowaæ,
jak z rstunnelem, aby go uruchomiæ. Monitorowanie po³±czenia u¿ywa
pêtli przekazywania portów. Czêstotliwo¶æ prób po³±czeñ jest
zmniejszana w przypadku napotkania nag³ych awarii, takich jak
odrzucenie po³±czenia. Program skompilowano i sprawdzono na OpenBSD,
Linuksie i Solarisie; powinien dzia³aæ tak¿e na innych BSD (oprócz
MacOS 10).

%prep
%setup -q

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
