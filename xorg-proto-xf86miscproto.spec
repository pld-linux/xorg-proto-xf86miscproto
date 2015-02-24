Summary:	XFree86-Misc extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XFree86-Misc
Name:		xorg-proto-xf86miscproto
Version:	0.9.3
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86miscproto-%{version}.tar.bz2
# Source0-md5:	ca63bbb31cf5b7f37b2237e923ff257a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes the protocol definitions of the "XFree86-Misc"
extension to the X11 protocol. The "XFree86-Misc" extension is
supported by the XFree86 X server and versions of the Xorg X server
prior to Xorg 1.6.

%description -l pl.UTF-8
Ten pakiet zawiera definicje protokołu rozszerzenia "XFree86-Misc"
do protokołu X11. Rozszerzenie to jest obsługiwane przez serwer X
XFree86 oraz serwer X Xorg w wersji wcześniejszej niż Xorg 1.6.

%package devel
Summary:	XFree86-Misc extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XFree86-Misc
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
This package includes the protocol definitions of the "XFree86-Misc"
extension to the X11 protocol. The "XFree86-Misc" extension is
supported by the XFree86 X server and versions of the Xorg X server
prior to Xorg 1.6.

%description devel -l pl.UTF-8
Ten pakiet zawiera definicje protokołu rozszerzenia "XFree86-Misc"
do protokołu X11. Rozszerzenie to jest obsługiwane przez serwer X
XFree86 oraz serwer X Xorg w wersji wcześniejszej niż Xorg 1.6.

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
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/xf86mscstr.h
%{_includedir}/X11/extensions/xf86misc.h
%{_pkgconfigdir}/xf86miscproto.pc
