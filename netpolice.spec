Name:		netpolice
Version:	2.0
Release:	4

Summary:	Netpolice is content filtering system
License:	BSD
Group:		System/Servers
Url:		https://www.netpolice.ru/

Source0:	readme

%description
Netpolice is content filtering system.

Requires:	%{name} = %{version}-%{release}

%package -n %{name}-main
Summary:	netpolice meta package
Group:		System/Servers 
Requires:	squid >= 3.0
Requires:	memcached
Requires:	c-icap-server >= 0.1.6
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
* Wed Dec 07 2011 Pischulin Anton <apischulin@mandriva.org> 2.0-2
+ Revision: 738486
- update netpolice to 2.0

  + Alex Burmashev <burmashev@mandriva.org>
    - import netpolice

