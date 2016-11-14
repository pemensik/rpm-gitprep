Name:		rpm-gitprep
Version:	0.1
Release:	2%{?dist}
Summary:	Prepare your RPM sources into git repository

#Group:		
License:	GPLv3+
URL:		none
Source0:	rpmpatch.git
Source1:	rpmfixperms.git
Source2:	macros-rpm-gitprep

BuildArch:	noarch
BuildRequires:	rpm
Requires:	rpm

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
%{__install} -p rpmpatch.git %{buildroot}/%{execpath}/
%{__install} -p rpmfixperms.git %{buildroot}/%{execpath}/
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
%{__install} -p macros-rpm-gitprep %{buildroot}/%{_rpmconfigdir}/macros.d/

%files
%doc README.txt
%license COPYING
%{_libexecdir}/%{name}
%{_rpmconfigdir}/macros.d/macros-rpm-gitprep

%changelog
* Mon Nov 14 2016 Petr Menšík <pemensik@redhat.com> - 0.1-2
- Initial package


