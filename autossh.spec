Summary:	Automatically restart SSH sessions and tunnels
Summary(pl.UTF-8):	Automatyczny restart sesji i tuneli SSH
Name:		autossh
Version:	1.4c
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
# Source0-md5:	26520eea934f296be0783dabe7fcfd28
Source1:	%{name}.init
Source2:	%{name}.tab
Source3:	%{name}.tmpfiles
URL:		http://www.harding.motd.ca/autossh/
BuildRequires:	rpmbuild(macros) >= 1.647
Requires:	openssh-clients
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

%package init
Summary:	autossh configuration as system service
Summary(pl.UTF-8):	konfiguracja autossh jako usługi systemowej
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	awk
Requires:	rc-scripts >= 0.4.0.20

%description init
this package contains init script and example configuration file, that
allows to run autossh as Unix system service.

%description init -l pl.UTF-8
Ten pakiet zawiera skrypt startowy oraz przykładowy plik
konfiguracyjny, które pozwalają uruchamić autossh jako uniksową usługę
systemową.

%prep
%setup -q

%build
%configure \
	--with-ssh=/usr/bin/ssh
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/var/run/%{name},%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/autossh.tab
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

install -p autossh $RPM_BUILD_ROOT%{_bindir}
cp -p autossh.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post init
/sbin/chkconfig --add autossh
%service autossh restart "autossh"

%preun init
if [ "$1" = "0" ]; then
	%service autossh stop
	/sbin/chkconfig --del autossh
fi

%files
%defattr(644,root,root,755)
%doc README CHANGES autossh.host rscreen
%attr(755,root,root) %{_bindir}/autossh
%{_mandir}/man1/autossh.1*

%files init
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.tab
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%{systemdtmpfilesdir}/%{name}.conf
%dir /var/run/autossh
