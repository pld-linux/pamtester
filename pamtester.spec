Summary:	Utility for testing pluggable authentication modules (PAM) facility
Name:		pamtester
Version:	0.1.2
Release:	0.1
License:	GPL
Group:		Base
URL:		http://pamtester.sourceforge.net/
Source0:	http://dl.sourceforge.net/pamtester/%{name}-%{version}.tar.gz
# Source0-md5:	f441a6617cbc640ea02f3e22058c0461
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pamtester is a tiny utility program to test the pluggable
authentication modules (PAM) facility, which is a de facto standard of
unified authentication management mechanism in many unices and similar
OSes.

While specifically designed to help PAM module authors to test their
modules, that might also be handy for system administrators interested
in building a centralised authentication system using common standards
such as NIS, SASL and LDAP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%{_mandir}/man1/pamtester.1*
%attr(755,root,root) %{_bindir}/pamtester