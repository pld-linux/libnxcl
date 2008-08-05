Summary:	A Library for building NoMachine (NX) clients
Name:		libnxcl
Version:	0.9
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://download.berlios.de/freenx/freenx-client-%{version}.tar.bz2
# Source0-md5:	777b3cda7a245e3870d4870a9460cb73
Patch0:		%{name}-stdlib.patch
URL:		http://freenx.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Library for building NoMachine (NX) clients

%package devel
Summary:	Header files for ... library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ...
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nxcl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nxcl

%package static
Summary:	Static nxcl library
Summary(pl.UTF-8):	Statyczna biblioteka nxcl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nxcl library.

%description static -l pl.UTF-8
Statyczna biblioteka nxcl

%prep
%setup -q -n freenx-client-%{version}
%patch0 -p1

%build
cd nxcl
%{__aclocal}
%{__autoheader}
%{__autoconf}
libtoolize --copy --automake
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd nxcl
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libnxcl.so.*

%files devel
%defattr(644,root,root,755)
%_libdir/libnxcl.so
%{_includedir}/nxcl
%_libdir/libnxcl.la
%_libdir/pkgconfig/nxcl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnxcl.a
