Name:		python-fsspec
Version:	2026.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fsspec/fsspec-%{version}.tar.gz
Summary:	File-system specification
URL:		https://pypi.org/project/fsspec/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
File-system specification

%files
%{py_sitedir}/fsspec
%{py_sitedir}/fsspec-*.*-info
