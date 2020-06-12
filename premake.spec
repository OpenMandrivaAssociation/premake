%define pre_rel beta5

Summary:	Build script generator
Name:		premake
Version:	4.4
Release:	%{?pre_rel:0.%{pre_rel}.}1
License:	GPL
Group:		Development/Other
URL:            http://premake.github.io/
Source0:        http://downloads.sourceforge.net/%{name}/premake-%{version}%{?pre_rel:-%{pre_rel}}-src.zip
Patch0:         premake-4.4-use-system-lua.patch
Patch1:         premake-4.3-manpage.patch
Patch2:         premake-4.4-parallel-build.patch


BuildRequires:  doxygen
BuildRequires:  pkgconfig(luajit)
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
%autosetup -p1 -n %{name}-%{version}%{?pre_rel:-%{pre_rel}}

# do not strip the executable
sed -i -e "s|\$(LDFLAGS) -L. -s|\$(LDFLAGS) -L.|" build/gmake.unix/Premake4.make

%build
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
%{_mandir}/man1/premake4.1*
