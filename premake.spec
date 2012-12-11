Summary:	Build script generator
Name:		premake
Version:	3.2
Release:	%mkrel 6
License:	GPL
Group:		Development/Other
URL:		http://premake.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/premake/%{name}-src-%{version}.zip
BuildRequires:	lua-devel
BuildRoot:	%{_tmppath}/%{name}-root

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

%setup -q -n Premake-%{version}

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build

%make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" -C Src

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 bin/%{name} %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt README.txt
%attr(0755,root,root) %{_bindir}/%{name}




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

