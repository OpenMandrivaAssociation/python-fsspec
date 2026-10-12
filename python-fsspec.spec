Name:		python-fsspec
Version:	2026.9.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fsspec/fsspec-%{version}.tar.gz
Summary:	File-system specification
URL:		https://pypi.org/project/fsspec/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
File-system specification

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/fsspec
%{py_sitedir}/fsspec-*.*-info
