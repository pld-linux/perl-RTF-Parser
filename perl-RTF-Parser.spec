%include	/usr/lib/rpm/macros.perl
%define	pdir	RTF
%define	pnam	Parser
Summary:	RTF::Parser Perl module
Summary(cs):	Modul RTF::Parser pro Perl
Summary(da):	Perlmodul RTF::Parser
Summary(de):	RTF::Parser Perl Modul
Summary(es):	Módulo de Perl RTF::Parser
Summary(fr):	Module Perl RTF::Parser
Summary(it):	Modulo di Perl RTF::Parser
Summary(ja):	RTF::Parser Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	RTF::Parser ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul RTF::Parser
Summary(pl):	Modu³ Perla RTF::Parser
Summary(pt):	Módulo de Perl RTF::Parser
Summary(pt_BR):	Módulo Perl RTF::Parser
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl RTF::Parser
Summary(sv):	RTF::Parser Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl RTF::Parser
Summary(zh_CN):	RTF::Parser Perl Ä£¿é
Name:		perl-RTF-Parser
Version:	1.07
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RTF::Parser - RTF Processor.

%description -l pl
RTF::Parser - procesor dokumentów w formacie RTF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/rtf2html
%{perl_vendorlib}/RTF
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
