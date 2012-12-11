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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.15-5mdv2010.0
+ Revision: 445100
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.15-4mdv2009.1
+ Revision: 350115
- 2009.1 rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.15-3mdv2009.0
+ Revision: 239156
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jun 26 2006 Oden Eriksson <oeriksson@mandriva.com> 1.15-2mdv2007.0
- rebuild

* Thu May 05 2005 Oden Eriksson <oeriksson@mandriva.com> 1.15-2mdk
- rebuilt with gcc4

* Sun Dec 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.15-1mdk
- initial mandrake package

