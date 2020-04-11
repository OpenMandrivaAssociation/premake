%define pre_rel beta5

Summary:	Build script generator
Name:		premake
Version:	4.4
Release:	%mkrel -c %{pre_rel} 1
License:	GPL
Group:		Development/Other
URL:            http://industriousone.com/premake
Source0:        http://downloads.sourceforge.net/%{name}/premake-%{version}-%{pre_rel}-src.zip
Patch0:         premake-4.4-mga-fdr-system-lua.patch

BuildRequires:  doxygen
BuildRequires:  pkgconfig(lua) > 5.0
BuildRequires:  pkgconfig(lua) < 5.2
#BuildRequires:  lua-devel
BuildRequires:  readline-devel

%description
Premake is a build script generator. Describe your project using the
full-featured Lua scripting language and then let Premake create the input
files for:

 * MS Visual Studio 6, 2002, 2003, or 2005
 * GNU make (including Cygwin and MinGW)
 * IC#Code SharpDevelop
 * MonoDevelop
 * ...more on the way!

%prep
%setup -q -n %{name}-%{version}-%{pre_rel}
%autopatch -p1

# do not stripping the executable
sed -i -e "s|\$(LDFLAGS) -L. -s|\$(LDFLAGS) -L.|" build/gmake.unix/Premake4.make

%build
#export CC=gcc
#export CXX=g++

pushd build/gmake.unix/
%set_build_flags
%make
popd

# Generate doc
doxygen

%install
install -m 755 -Dp ./bin/release/premake4 %{buildroot}/%{_bindir}/premake4
install -m 644 -Dp ./premake4.1 %{buildroot}/%{_mandir}/man1/premake4.1

%files
%doc doc/html/* LICENSE.txt README.txt CHANGES.txt
%{_bindir}/premake4
%{_mandir}/man1/premake4.1.*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.2-6mdv2010.0
+ Revision: 430779
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-5mdv2009.0
+ Revision: 259285
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-4mdv2009.0
+ Revision: 247215
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-2mdv2008.1
+ Revision: 171051
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.2-1mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2-1mdv2007.0
+ Revision: 133985
- fix build
- Import premake

* Tue Mar 06 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2-1mdv2007.1
- initial Mandriva package

