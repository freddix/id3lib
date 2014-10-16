# based on PLD Linux spec git://git.pld-linux.org/packages/id3lib.git
Summary:	Library for manipulating ID3v1 and ID3v2 tags
Name:		id3lib
Version:	3.8.3
Release:	13
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
# Source0-md5:	19f27ddd2dda4b2d26a559a4f0f402a7
Patch0:		%{name}-nozlibpopt.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		http://heanet.dl.sourceforge.net/easytag/patch_id3lib_3.8.3_UTF16_writing_bug.diff
Patch4:		%{name}-gcc43.patch
URL:		http://id3lib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities.

%package devel
Summary:	Headers for developing programs that will use id3lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to
develop applications which will use id3lib, the software library for
ID3v1 and ID3v2 tag manipulation.

%package utils
Summary:	Simple id3 utils
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
Few simple utilities to manipulate on ID3 tags: id3convert, id3cp,
id3info, id3tag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

