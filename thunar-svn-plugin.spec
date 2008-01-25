Summary:	A svn plugin for Thunar file manager
Name:		thunar-svn-plugin
Version:	0.0.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/releases/thunar-svn-plugin/thunar-svn-plugin-0.0.1.tar.bz2
Source0:	http://goodies.xfce.org/releases/thunar-svn-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A svn plugin for Thunar file manager

%prep
%setup -q %{name}-%{version}

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc
%attr(755,root,root)
