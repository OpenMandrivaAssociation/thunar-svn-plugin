Summary:	A svn plugin for Thunar file manager
Name:		thunar-svn-plugin
Version:	0.0.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/thunar-svn-plugin
Source0:	http://goodies.xfce.org/releases/thunar-svn-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel
BuildRequires:	%{_lib}svn-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A svn plugin for Thunar file manager.

%prep
%setup -q %{name}-%{version}

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/thunarx-1/thunar-svn-plugin.*
%{_libdir}/tsp-svn-helper
%{_iconsdir}/hicolor/*/apps/*.png
