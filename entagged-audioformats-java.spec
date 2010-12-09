%define shortname entagged-audioformats
Name:		%{shortname}-java
Version:	0.15
Release:	%mkrel 6
License:	LGPLv2+
URL:		http://entagged.sourceforge.net/
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

