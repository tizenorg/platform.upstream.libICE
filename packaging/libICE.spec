Name:           libICE
Version:        1.0.8
Release:        0
License:        MIT
Summary:        X11 Inter-Client Exchange Library
Url:            http://xorg.freedesktop.org/
Group:          Development/Libraries/C and C++

Source:         %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)

%description
There are numerous possible inter-client protocols, with many
similarities and common needs - authentication, version negotiation,
byte order negotiation, and so on.
The Inter-Client Exchange (ICE) protocol is intended to provide a
framework for building such protocols, allowing them to make use of
common negotiation mechanisms and to be multiplexed over a single
transport connection.

%package devel
Summary:        Development files for the X11 Inter-Client Exchange Library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The Inter-Client Exchange (ICE) protocol is intended to provide a
framework for building such protocols, allowing them to make use of
common negotiation mechanisms and to be multiplexed over a single
transport connection.

This package contains the development headers for the library found
in %{name}.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libICE.so.6*

%files devel
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%_docdir/%{name}

%changelog
