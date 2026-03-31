%define module markdown

Name:		python-markdown
Summary:	Python implementation of the markdown text-to-HTML conversion tool
Version:	3.10.2
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/Python-Markdown/markdown
Source:		%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This is a Python implementation of John Gruber's Markdown. It is almost 
completely compliant with the reference implementation, though there 
are a few known issues

Markdown  is a text-to-HTML conversion tool for web writers. Markdown 
allows you to write using an easy-to-read, easy-to-write plain text format, 
then convert it to structurally valid XHTML (or HTML).

%files 
%{_bindir}/markdown_py
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
