Summary:	A GNOME panel applet for connecting to hosts using SSH
Name:		gnome-applet-sshmenu
Version:	3.18
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://downloads.sourceforge.net/sshmenu/sshmenu-%{version}.tar.gz
# Source0-md5:	7e7f43135fd112be3c173ec8585d6b98
Patch0:		%{name}-ruby19.patch
Patch1:		%{name}-undebianize.patch
Patch2:		%{name}-pixmap.patch
URL:		http://sshmenu.sourceforge.net/
BuildRequires:	ruby-modules
Requires:	ruby-gnome2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSHMenu is a GNOME panel applet that keeps all your regular SSH
connections within a single mouse click.

%package -n bash-completion-sshmenu
Summary:	bash-completion for sshmenu
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla sshmenu
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-sshmenu
This package provides bash-completion for sshmenu.

%description -n bash-completion-sshmenu -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla sshmenu.

%prep
%setup -q -n sshmenu-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

sed -i -e 's|/usr/lib$|%{_libdir}/|g' \
       -e 's|gnome-panel/sshmenu-applet|sshmenu-applet|g' Makefile
sed -i -e 's|/usr/lib/gnome-panel|%{_libdir}|g' sshmenu-applet.server

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/ruby/{1.8,1.9}

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT{%{_iconsdir}/hicolor/48x48/apps,%{_pixmapsdir}}/gnome-sshmenu-applet.png

echo ".so sshmenu.1" >$RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/sshmenu*
%{_libdir}/bonobo/servers/*.server
%{ruby_rubylibdir}/*sshmenu.rb
%attr(755,root,root) %{_libdir}/sshmenu-applet
%{_pixmapsdir}/gnome-sshmenu-applet.png
%{_mandir}/man1/*sshmenu*.1*

%files -n bash-completion-sshmenu
%defattr(644,root,root,755)
/etc/bash_completion.d/sshmenu
