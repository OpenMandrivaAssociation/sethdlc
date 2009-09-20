Summary:	Sethdlc utility for 2.4/2.6 kernels
Name:		sethdlc
Version:	1.15
Release:	%mkrel 5
License:	GPL
Group:          System/Kernel and hardware
URL:		http://hq.pm.waw.pl/hdlc/
Source0:	http://hq.pm.waw.pl/hdlc/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Sethdlc utility for 2.4/2.6 kernels. The sethdlc utility is used to configure
certain HDLC cards. General HDLC layer for Linux is an interface between
low-level hardware drivers for synchronous serial (HDLC) cards and the rest of
kernel networking.

%prep

%setup -q -n %{name}-%{version}

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 sethdlc %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/sethdlc
