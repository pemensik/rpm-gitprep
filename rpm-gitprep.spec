Name:		rpm-gitprep
Version:	0.1
Release:	10%{?dist}
Summary:	Prepare your RPM sources into git repository

#Group:		
License:	GPLv3+
URL:		none
Source0:	rpmpatch.git
Source1:	macros.rpm-gitprep
Source2:	README.md
Source3:	COPYING
Source4:	spec-add-patch
Source5:	spec-changelog
Source6:	git-commit-url
Source7:	rej-solve
Source8:	git-commit-export

BuildArch:	noarch
BuildRequires:	rpm
Requires:	rpm
Requires:	rpmdevtools
Requires:	git-core

%description
This tool helps you to prepare your sources using rpmbuild -bp or 
fedpkg prep as git repository. It allows you to use git tools to 
analyze what patches of package changed. Or what files were 
modified by what patches.

%prep
[ -f "README.md" ] || install %{SOURCE2} README.md
[ -f "COPYING" ]   || install %{SOURCE3} COPYING

%build


%install
%define execpath %{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{execpath}
%{__install} -p %{SOURCE0} %{buildroot}/%{execpath}/
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
%{__install} -p %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_bindir}
%{__install} -pm 755 %{SOURCE4} %{buildroot}%{_bindir}/spec-add-patch
%{__install} -pm 755 %{SOURCE5} %{buildroot}%{_bindir}/spec-changelog
%{__install} -pm 755 %{SOURCE6} %{buildroot}%{_bindir}/git-commit-url
%{__install} -pm 755 %{SOURCE7} %{buildroot}%{_bindir}/rej-solve
%{__install} -pm 755 %{SOURCE8} %{buildroot}%{_bindir}/git-commit-export

%files
%doc README.md
%license COPYING
%{_libexecdir}/%{name}
%{_rpmconfigdir}/macros.d/macros.rpm-gitprep
%{_bindir}/spec-add-patch
%{_bindir}/spec-changelog
%{_bindir}/rej-solve
%{_bindir}/git-commit-url
%{_bindir}/git-commit-export

%changelog
* Sat Mar 02 2024 Petr Menšík <pemensik@redhat.com> - 0.1-10
- Commit changes done after section

* Tue Feb 21 2023 Petr Menšík <pemensik@redhat.com> - 0.1-9
- Avoid applying gitprep when  %autosetup -S git macro is used

* Mon May 30 2022 Petr Menšík <pemensik@redhat.com> - 0.1-8
- Add git-commit-export helper

* Wed Jul 17 2019 Petr Menšík <pemensik@redhat.com> - 0.1-7
- Add helper tools rej-solve and git-commit-url

* Wed Feb 06 2019 Petr Menšík <pemensik@redhat.com> - 0.1-6
- Add support for autosetup scm

* Mon Mar 05 2018 Petr Menšík <pemensik@redhat.com> - 0.1-5
- Add spec-changelog tool for dist-git bumping

* Fri Jul 07 2017 Petr Menšík <pemensik@redhat.com> - 0.1-4
- Add spec-add-patch to package

* Tue Nov 15 2016 Petr Menšík <pemensik@redhat.com> - 0.1-3
- Use patch directly, git apply is not powerful enough
- Replace rpmfixperms with RPM macro

* Mon Nov 14 2016 Petr Menšík <pemensik@redhat.com> - 0.1-2
- Initial package


