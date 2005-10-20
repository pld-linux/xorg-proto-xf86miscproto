Summary:	XF86Misc protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86Misc i pomocnicze
Name:		xorg-proto-xf86miscproto
Version:	0.9.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xf86miscproto-%{version}.tar.bz2
# Source0-md5:	4abf4c8338ae6319c14fb6661c4f35f0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
