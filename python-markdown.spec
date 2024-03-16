%define oname Markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool
Name: python-markdown
Version:	3.6
Release:	1
Source:  https://files.pythonhosted.org/packages/source/M/Markdown/%oname-%version.tar.gz
License: BSD
Group: Development/Python
BuildRequires: pkgconfig(python)
BuildRequires: python-pkg-resources
BuildRequires: python-setuptools
BuildRequires: python-nose
BuildRequires: python-yaml
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
%setup -q -n %oname-%version 
# remove shebangs
find markdown -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;

# fix line-ending
find docs -type f \
  -exec sed -i 's/\r//' {} \;

%build
%py_build

%install
%py_install

# rename binary
mv %{buildroot}%{_bindir}/markdown_py{,-%{python3_version}}
ln -s markdown_py-%{python3_version} %{buildroot}%{_bindir}/markdown_py-3
ln -s markdown_py-%{python3_version} %{buildroot}%{_bindir}/markdown_py

%files 
%{python_sitelib}/*
%{_bindir}/markdown_py-%{python_version}
%{_bindir}/markdown_py-3
%{_bindir}/markdown_py
