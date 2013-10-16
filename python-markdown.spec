%define name python-markdown
%define version 2.1.1
%define release 1
%define oname Markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool
Name: %{name}
Version: 2.3.1
Release: 1
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



%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1.1-1
+ Revision: 778154
- version update 2.1.1

* Mon Dec 05 2011 Lev Givon <lev@mandriva.org> 2.1.0-2
+ Revision: 737953
- Include egg info files to satisfy reqs of other packages.

* Mon Dec 05 2011 Lev Givon <lev@mandriva.org> 2.1.0-1
+ Revision: 737915
- Update to 2.1.0.

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0.3-2mdv2011.0
+ Revision: 592470
- rebuild to get correct auto requries

* Sat Mar 13 2010 Michael Scherer <misc@mandriva.org> 2.0.3-1mdv2010.1
+ Revision: 518607
- update to 2.0.3

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.6a-1mdv2010.0
+ Revision: 136450
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Michael Scherer <misc@mandriva.org>
    - add missing egg-info
    - Import python-markdown


