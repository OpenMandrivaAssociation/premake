Summary:	Build script generator
Name:		premake
Version:	3.2
Release:	%mkrel 4
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


