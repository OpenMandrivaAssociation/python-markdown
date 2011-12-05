%define name python-markdown
%define version 2.1.0
%define release %mkrel 2
%define oname Markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool
Name: %{name}
Version: %{version}
Release: %{release}
Source:  http://pypi.python.org/packages/source/M/%{oname}/%{oname}-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpython-devel
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc docs 

