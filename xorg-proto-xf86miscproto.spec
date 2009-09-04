Summary:	XF86Misc protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86Misc i pomocnicze
Name:		xorg-proto-xf86miscproto
Version:	0.9.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86miscproto-%{version}.tar.bz2
# Source0-md5:	acae8edeb05a406f7f60bcbb218a8f1d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86Misc protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu XF86Misc i pomocnicze.

%package devel
Summary:	XF86Misc protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86Misc i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86Misc protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu XF86Misc i pomocnicze.

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86miscproto.pc
