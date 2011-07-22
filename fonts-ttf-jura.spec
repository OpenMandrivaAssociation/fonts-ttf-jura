%define pkgname jura-ttf

Summary: Family of sans-serif fonts in the Eurostile vein
Name: fonts-ttf-jura
Version: 2.4
Release: %mkrel 1
License: OFL & GPLv3
Group: System/Fonts/True type
URL: http://io.debian.net/~danielj/
Source0: http://io.debian.net/~danielj/jura/%{pkgname}-%{version}.tbz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
Jura is a family of sans-serif fonts in the Eurostile vein. It was originally inspired by some work I was doing for the FreeFont project in designing a Kayah Li range for FreeMono. (Kayah Li is a language used by a minority people group in Burma. Because the Burmese government suppresses the teaching of minority scripts, the Kayah Li script is taught only in schools in refugee camps in Thailand.) I wanted to create a Roman alphabet using the same kinds of strokes and curves as the Kayah Li glyphs, and thus Jura was born. It has been expanded to include glyphs for the Cyrillic and Greek alphabets as well.
Jura is available in four weights: Book, Medium, DemiBold, and Bold.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/jura

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/jura
ttmkfdir %{buildroot}%{_xfontdir}/TTF/jura > %{buildroot}%{_xfontdir}/TTF/jura/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/jura/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/jura \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-jura:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt license-gpl-3.0.txt license-ofl.txt
%dir %{_xfontdir}/TTF/jura
%{_xfontdir}/TTF/jura/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/jura/fonts.dir
%{_xfontdir}/TTF/jura/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-jura:pri=50



