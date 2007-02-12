Summary:	Automatically restart SSH sessions and tunnels
Summary(pl.UTF-8):   Automatyczny restart sesji i tuneli SSH
Name:		autossh
Version:	1.4a
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		Carson Harding <carson.harding@shaw.ca>
Source0:	http://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
# Source0-md5:	a5497938986f0c179926f1ebba603767
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

%description -l pl.UTF-8
autossh jest programem uruchamiającym kopię ssh i monitorującym ją,
restartując w miarę potrzeby, jeśli umrze lub przestanie przekazywać
ruch. Idea i mechanizm pochodzą z rstunnela (Reliable SSH Tunnel), ale
zaimplementowano je w C. Według autora nie trzeba się tak patyczkować,
jak z rstunnelem, aby go uruchomić. Monitorowanie połączenia używa
pętli przekazywania portów. Częstotliwość prób połączeń jest
zmniejszana w przypadku napotkania nagłych awarii, takich jak
odrzucenie połączenia. Program skompilowano i sprawdzono na OpenBSD,
Linuksie i Solarisie; powinien działać także na innych BSD (oprócz
MacOS 10).

%prep
%setup -q

%build
%configure
%{__make} 

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
