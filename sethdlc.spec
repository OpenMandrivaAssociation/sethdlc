%define	debug_package	%nil

Summary:	Sethdlc utility for 2.4/2.6 kernels
Name:		sethdlc
Version:	1.18
Release:	8
License:	GPLv2+
Group:          System/Kernel and hardware
URL:		http://hq.pm.waw.pl/hdlc/
Source0:	http://www.kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.tar.gz
Source1:	http://www.kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.tar.gz.sign
Patch0:		sethdlc-no-kernel-headers.patch

%description
Sethdlc utility for 2.4/2.6 kernels. The sethdlc utility is used to configure
certain HDLC cards. General HDLC layer for Linux is an interface between
low-level hardware drivers for synchronous serial (HDLC) cards and the rest of
kernel networking.

%prep

%setup -q -n %{name}-%{version}
%apply_patches
# remove prebuilt binary included in the tarball
rm -f sethdlc

%build
%setup_compile_flags
%make CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -m0755 sethdlc %{buildroot}%{_bindir}/

%files
%{_bindir}/sethdlc
