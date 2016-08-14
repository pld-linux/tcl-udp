Summary:	Create UDP sockets in Tcl
Name:		tcl-udp
Version:	1.0.11
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcludp/tcludp-%{version}.tar.gz
# Source0-md5:	945ea7afd1df9e46090733ffbfd724a1
Patch0:		%{name}-man.patch
URL:		http://tcludp.sourceforge.net/
BuildRequires:	tcl-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tcl UDP extension provides a simple library to support UDP socket
in Tcl.

%prep
%setup -q -n tcludp
%patch0 -p1

%build
%configure \
	--enable-64bit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/udp*
%attr(755,root,root) %{_libdir}/udp*/libudp*.so
%{_libdir}/udp*/*.tcl
%{_mandir}/man*/udp*
