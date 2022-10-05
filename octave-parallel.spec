%global octpkg parallel

Summary:	Parallel execution package for Octave
Name:		octave-%{octpkg}
Version:	4.0.1
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?61516
Patch0:		honor-cflags-cppflags-cxxflags.patch
# https://savannah.gnu.org/bugs/?62349
Patch1:		parallel-4.0.1-fix_octave_7.patch
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	octave-struct >= 1.0.12
BuildRequires:	pkgconfig(p11-kit-1)

Requires:	octave(api) = %{octave_api}
Requires:	octave-struct >= 1.0.12

Requires(post): octave
Requires(postun): octave

%description
Parallel execution package for Octave. See also package octave-mpi.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

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

