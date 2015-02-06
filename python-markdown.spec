%define oname Markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool

Name: python-markdown
Version: 2.4.1
Release: 2
Source0:  http://pypi.python.org/packages/source/M/Markdown/Markdown-%{version}.tar.gz
License: BSD
Group: Development/Python
Url: http://www.freewisdom.org/projects/python-markdown/ 
BuildArch: noarch

%description
This is a Python implementation of John Gruber's Markdown. It is almost 
completely compliant with the reference implementation, though there 
are a few known issues

Markdown  is a text-to-HTML conversion tool for web writers. Markdown 
allows you to write using an easy-to-read, easy-to-write plain text format, 
then convert it to structurally valid XHTML (or HTML).

%prep
%setup -q -n %{oname}-%{version} 

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%doc docs 




