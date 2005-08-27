Summary:	XF86Misc protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86Misc i pomocnicze
Name:		xorg-proto-xf86miscproto
Version:	0.9
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/xf86miscproto-%{version}.tar.bz2
# Source0-md5:	3ea64e4a9a04881fff49152726be98da
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XF86Misc protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XF86Misc i pomocnicze.

%package devel
Summary:	XF86Misc protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86Misc i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86Misc protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XF86Misc i pomocnicze.

%prep
%setup -q -n xf86miscproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86miscproto.pc
