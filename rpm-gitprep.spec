Name:		rpm-gitprep
Version:	0.1
Release:	4%{?dist}
Summary:	Prepare your RPM sources into git repository

#Group:		
License:	GPLv3+
URL:		none
Source0:	rpmpatch.git
Source1:	macros.rpm-gitprep
Source2:	README.txt
Source3:	COPYING
Source4:	spec-add-patch

BuildArch:	noarch
BuildRequires:	rpm
Requires:	rpm
Requires:	rpmdevtools

%description
This tool helps you to prepare your sources using rpmbuild -bp or 
fedpkg prep as git repository. It allows you to use git tools to 
analyze what patches of package changed. Or what files were 
modified by what patches.

%prep


%build


%install
%define execpath %{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{execpath}
%{__install} -p %{SOURCE0} %{buildroot}/%{execpath}/
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
%{__install} -p %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 755 %{SOURCE4} %{buildroot}%{_bindir}/spec-add-patch

%files
%doc README.txt
%license COPYING
%{_libexecdir}/%{name}
%{_rpmconfigdir}/macros.d/macros.rpm-gitprep
%{_bindir}/spec-add-patch

%changelog
* Fri Jul 07 2017 Petr Menšík <pemensik@redhat.com> - 0.1-4
- Add spec-add-patch to package

* Tue Nov 15 2016 Petr Menšík <pemensik@redhat.com> - 0.1-3
- Use patch directly, git apply is not powerful enough
- Replace rpmfixperms with RPM macro

* Mon Nov 14 2016 Petr Menšík <pemensik@redhat.com> - 0.1-2
- Initial package


