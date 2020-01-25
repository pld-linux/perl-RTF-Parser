#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	RTF
%define		pnam	Parser
Summary:	RTF::Parser - RTF Processor
Summary(pl.UTF-8):	RTF::Parser - procesor dokumentów w formacie RTF
Name:		perl-RTF-Parser
Version:	1.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	249eda70ecb9fe5e9231d31c53587b31
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/RTF-Parser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-RTF-Tokenizer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RTF::Parser - RTF Processor.

%description -l pl.UTF-8
RTF::Parser - procesor dokumentów w formacie RTF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/rtf2html
%{perl_vendorlib}/RTF/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
%{_mandir}/*/*
