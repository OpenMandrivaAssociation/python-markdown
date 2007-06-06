%define name python-markdown
%define version 1.6a
%define release %mkrel 1
%define oname markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool
Name: %{name}
Version: %{version}
Release: %{release}
Source:  http://prdownloads.sourceforge.net/%name/%oname-%version.tar.bz2
License: GPL
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
%setup -q -n %oname-1.6 

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc CHANGE_LOG.txt README.txt home_page.txt
# example 
%doc  mdx_footnotes.py mdx_rss.py
%py_puresitedir/%oname.py*



