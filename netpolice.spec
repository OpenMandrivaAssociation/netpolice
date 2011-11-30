Name:		netpolice
Version:	2.0
Release:	2

Summary:	Netpolice is content filtering system
License:	BSD
Group:		System/Servers
BuildRoot:	%{_tmppatch}/%{name}-%{version}-%{release}-buildroot
Url:		http://www.netpolice.ru/

Source0:	readme

%description
Netpolice is content filtering system.

Requires:	%{name} = %{version}-%{release}

%package -n %{name}-main
Summary:	netpolice meta package
Group:		System/Servers 
Requires:	squid >= 3.0
Requires:	memcached
Requires:	c-icap >= 0.1.6
Requires:	netpolice-filter
Requires:	squid-conf-host2cat >= 1.01
Requires:	host2cat >= 1.01
Requires:	netpolice-webadmin

%description -n %{name}-main
This package is meta package for %{name}.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_docdir}
install -pD -m644 %{SOURCE0} %{buildroot}%{_docdir}/%{name}/%{name}

%clean
rm -rf %{buildroot}

%files -n %{name}-main
%defattr(-,root,root)
%doc %{_docdir}/%{name}/%{name}

%changelog
* Mon Aug 29 2011 L.Butorina <l.butorina@cair.ru> 2
- New test version netpolice-2.0 for Mandriva.

* Fri Jul 29 2011 L.Butorina <l.butorina@cair.ru> 1
- New test version netpolice for Mandriva.
