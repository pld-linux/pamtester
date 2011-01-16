Summary:	Utility for testing pluggable authentication modules (PAM) facility
Summary(pl.UTF-8):	Narzędzie do testowania modułów PAM
Name:		pamtester
Version:	0.1.2
Release:	1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/pamtester/%{name}-%{version}.tar.gz
# Source0-md5:	f441a6617cbc640ea02f3e22058c0461
URL:		http://pamtester.sourceforge.net/
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

%description -l pl.UTF-8
pamtester to mały program narzędziowy do testowania modułów PAM
(Pluggable Authentication Modules), będących standardem de facto
ujednoliconego mechanizmu uwierzytelniania w wielu systemach
uniksowych.

O ile program został napisany z myślą o pomocy autorom modułów PAM w
testowaniu ich modułów, może być także przydatny dla administratorów
systemów zainteresowanych tworzeniem scentralizowanego systemu
uwierzytelniania z użyciem popularnych standardów takich jak NIS, SASL
i LDAP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%attr(755,root,root) %{_bindir}/pamtester
%{_mandir}/man1/pamtester.1*
