# This is an unofficial package of the Python versions for PyPI
# https://bitbucket.org/spookylukey/diff-match-patch for packaging issues.
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	diff_match_patch
Summary:	The Diff Match and Patch libraries
Name:		python-%{module}
Version:	20121119
Release:	3
License:	ASL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/22/82/46eaeab04805b4fac17630b59f30c4f2c8860988bcefd730ff4f1992908b/diff-match-patch-%{version}.tar.gz
# Source0-md5:	08e02cad82dda942b09ee248772fe143
URL:		https://code.google.com/p/google-diff-match-patch/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Diff Match and Patch libraries offer robust algorithms to perform
the operations required for synchronizing plain text.

%package -n python3-%{module}
Summary:	The Diff Match and Patch libraries
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
The Diff Match and Patch libraries offer robust algorithms to perform
the operations required for synchronizing plain text.

%prep
%setup -q -n diff-match-patch-%{version}

# Remove bundled egg-info
%{__rm} -r python2/diff_match_patch.egg-info

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README.original.txt README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.original.txt README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
