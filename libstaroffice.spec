%define api	0.0
%define major	0
%define libname	%mklibname staroffice %{api} %{major}
%define devname	%mklibname -d staroffice

Summary:	Library for importing and converting StarOffice files
Name:		libstaroffice
Epoch:		1
Version:	0.0.6
Release:	1
Group:		Office
License:	LGPLv2+
Url:		https://github.com/fosnola/libstaroffice
Source0:	https://github.com/fosnola/libstaroffice/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel

%description
A library for reading and converting StarOffice files

%package tools
Summary:	Tools to convert StarOffice files into other formats
Group:		Publishing

%description tools
Tools to convert StarOffice files into other formats.

%package -n %{libname}
Summary:	Library for importing and converting StarOffice files
Group:		System/Libraries

%description -n %{libname}
A library for reading and converting StarOffice files

%package -n %{devname}
Summary:	Files for developing with libstaroffice
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Includes and definitions for developing with libstaroffice.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure
%make 

%install
%makeinstall_std

%files tools
%doc ChangeLog README
%{_bindir}/sd2*
%{_bindir}/sdc2*
%{_bindir}/sdw2*

%files -n %{libname}
%{_libdir}/libstaroffice-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libstaroffice*.so
%{_libdir}/pkgconfig/libstaroffice*.pc
%{_includedir}/*
%doc %{_docdir}/libstaroffice/*
