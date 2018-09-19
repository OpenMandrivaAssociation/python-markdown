%define oname Markdown

Summary: Python implementation of the markdown text-to-HTML conversion tool
Name: python-markdown
Version: 2.6.11
Release: 1
Source:  https://files.pythonhosted.org/packages/source/M/Markdown/%oname-%version.tar.gz
License: BSD
Group: Development/Python
BuildRequires: pkgconfig(python2)
BuildRequires: python2-pkg-resources
BuildRequires: python2-nose
BuildRequires: python2-yaml
BuildRequires: pkgconfig(python)
BuildRequires: python-pkg-resources
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

%package -n python2-markdown
Summary: Python 2 implementation of the markdown text-to-HTML conversion tool
Group: Development/Python

%description -n python2-markdown
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

cp -a . %{py2dir}

%build
pushd %{py2dir}
%py2_build
popd

%py_build

%install
%py_install

# rename binary
mv %{buildroot}%{_bindir}/markdown_py{,-%{python3_version}}
ln -s markdown_py-%{python3_version} %{buildroot}%{_bindir}/markdown_py-3

pushd %{py2dir}
%py2_install
# rename binary
mv %{buildroot}%{_bindir}/markdown_py{,-%{python2_version}}
ln -s markdown_py-%{python2_version} %{buildroot}%{_bindir}/markdown_py-2
popd

# 2.X binary is called by default for now
ln -s markdown_py-%{python2_version} %{buildroot}%{_bindir}/markdown_py

%check
%{__python} run-tests.py

pushd %{py2dir}
%{__python2} run-tests.py
popd

%files 
%doc build/docs/
%{python_sitelib}/*
%{_bindir}/markdown_py-%{python_version}

%files -n python2-markdown
%doc build/docs/*
%{python2_sitelib}/*
%{_bindir}/markdown_py
%{_bindir}/markdown_py-%{python2_version}

