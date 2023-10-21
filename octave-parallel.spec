%global octpkg parallel

Summary:	Parallel execution package for Octave
Name:		octave-parallel
Version:	4.0.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/parallel/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/?62349
#Patch1:		parallel-4.0.1-fix_octave_8.patch
#Patch1:		parallel-4.0.1-fix_octave_8.2.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  octave-struct >= 1.0.12
BuildRequires:	parallel
BuildRequires:	pkgconfig(p11-kit-1)

Requires:	octave(api) = %{octave_api}
Requires:  	octave-struct >= 1.0.12
Requires:	parallel

Requires(post): octave
Requires(postun): octave

%description
Parallel execution package for Octave. See also package octave-mpi.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

