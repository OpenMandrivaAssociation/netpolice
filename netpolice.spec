%define _unpackaged_files_terminate_build 0 `

Name: netpolice
Version: 1.2
Release: 1%{?dist}
Packager: CAIR <support@cair.ru>

Summary: netpolice meta package 
License: BSD
Group: System/Servers
Url: http://www.netpolice.ru/

Source0: readme

BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
netpolice meta package.

%package -n %name-main
Summary: netpolice meta package
Group: System/Servers
Requires: squid >= 3.0
Requires: memcached
Requires: c-icap-netpolice-server
Requires: c-icap-netpolice-modules
Requires: netpolice-filter
Requires: squid-conf-host2cat
Requires: host2cat
Requires: libc-icap-netpolice0
Conflicts: c-icap-server
Conflicts: libc-icap0
Conflicts: c-icap-modules

%description -n %name-main
This is the netpolice meta package.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_docdir/netpolice
install -pD -m644 %SOURCE0 %buildroot%_docdir/netpolice

%files -n %name-main
%_docdir/netpolice/readme

