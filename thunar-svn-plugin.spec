%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A svn plugin for Thunar file manager
Name:		thunar-svn-plugin
Version:	0.0.3
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/thunar-svn-plugin
Source0:	http://archive.xfce.org/src/thunar-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		thunar-svn-plugin-0.0.3-rosa-thunarx-2.patch
Patch1:		thunar-svn-plugin-0.0.3-rosa-svn-includes.patch
Patch2:		thunar-svn-plugin-0.0.3-rosa-format-security.patch
BuildRequires:	pkgconfig(thunarx-2)
BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	subversion-devel
BuildRequires:	gtk+2-devel

# required for patch0
BuildRequires:	xfce4-dev-tools

%description
A svn plugin for Thunar file manager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

# required for patch0
xdt-autogen

%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_libdir}/thunarx-2/thunar-svn-plugin.*
%{_libdir}/tsp-svn-helper
%{_iconsdir}/hicolor/*/apps/*
