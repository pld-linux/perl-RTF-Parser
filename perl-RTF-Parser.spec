%include	/usr/lib/rpm/macros.perl
Summary:	RTF-Parser perl module
Summary(pl):	Modu³ perla RTF-Parser
Name:		perl-RTF-Parser
Version:	1.07
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/RTF/RTF-Parser-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RTF-Parser - RTF Processor.

%description -l pl
RTF-Parser - procesor dokumentów w formacie RTF.

%prep
%setup -q -n RTF-Parser-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/tests.pl
%attr(755,root,root) %{_bindir}/rtf2html
%{perl_sitelib}/RTF/*.pm
%{perl_sitelib}/RTF/HTML
