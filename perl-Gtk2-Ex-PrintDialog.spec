#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	Ex-PrintDialog
Summary:	A simple, pure Perl dialog for printing PostScript data in GTK+ applications
Summary(pl):	Proste, czysto perlowe okno dialogowe do drukowania PostScriptu z aplikacji GTK+
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc6749cbffb8b79450985419eac03928
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gtk2 >= 1.101-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, pure Perl dialog for printing PostScript data in GTK+
applications.

%description -l pl
Proste, czysto perlowe okno dialogowe do drukowania PostScriptu z
poziomu aplikacji GTK+.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Gtk2/Ex/PrintDialog.pm
%dir %{perl_vendorlib}/Gtk2/Ex/PrintDialog
%{perl_vendorlib}/Gtk2/Ex/PrintDialog/Darwin.pm
%{perl_vendorlib}/Gtk2/Ex/PrintDialog/Linux.pm
%{perl_vendorlib}/Gtk2/Ex/PrintDialog/Unix.pm
%{_mandir}/man3/*
