%define shortname entagged-audioformats
Name:		%{shortname}-java
Version:	0.15
Release:	7
License:	LGPLv2+
URL:		https://entagged.sourceforge.net/
Source:		entagged-audioformats-source-%{version}.tar.gz
Group:		Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	Library to access and modify tags in audio files
Requires:	java
BuildRequires:	java-devel ant
BuildArch:	noarch
%description
Java library to access and modify tags in audio files.

%prep
%setup -q -n entagged

%build
cd audioformats
%{_bindir}/ant

%install
%{__rm} -Rf %{buildroot}
cd audioformats
%{__mkdir_p} %{buildroot}%{_javadir}
ln -s %{shortname}-%{version}.jar %{shortname}.jar
%{__cp} -p %{shortname}-%{version}.jar %{shortname}.jar %{buildroot}%{_javadir}

%files
%{_javadir}/%{shortname}-%{version}.jar
%{_javadir}/%{shortname}.jar

%package -n %{shortname}-javadoc
Group:		Development/Java
Summary:	Javadoc for %{shortname}
%description -n %{shortname}-javadoc
javadoc for %{shortname}

%files -n %{shortname}-javadoc
%doc audioformats/javadoc



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15-6mdv2011.0
+ Revision: 618233
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.15-5mdv2010.0
+ Revision: 428627
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.15-4mdv2009.0
+ Revision: 240686
- rebuild
- fix summary-not-capitalized
- fix no-buildroot-tag

* Wed Sep 05 2007 Nicolas Vigier <nvigier@mandriva.com> 0.15-2mdv2008.0
+ Revision: 80038
- package is noarch

* Wed Sep 05 2007 Nicolas Vigier <nvigier@mandriva.com> 0.15-1mdv2008.0
+ Revision: 80018
- Import entagged-audioformats-java

