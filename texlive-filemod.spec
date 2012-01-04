# revision 24042
# category Package
# catalog-ctan /macros/latex/contrib/filemod
# catalog-date 2011-09-21 00:38:26 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-filemod
Version:	1.2
Release:	2
Summary:	Provide file modification times, and compare them
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/filemod
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filemod.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filemod.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros to read and compare the
modification dates of files. The files may be .tex files,
images or other files (as long as they can be found by LaTeX).
It uses the \pdffilemoddate primitive of pdfLaTeX to find the
file modification date as PDF date string, parses the string
and returns the value to the user. The package will also work
for DVI output with recent versions of the LaTeX compiler which
uses pdfLaTeX in DVI mode. The functionality is provided by
purely expandable macros or by faster but non-expandable ones.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/filemod/filemod-expmin.tex
%{_texmfdistdir}/tex/generic/filemod/filemod.tex
%{_texmfdistdir}/tex/latex/filemod/filemod-expmin.sty
%{_texmfdistdir}/tex/latex/filemod/filemod.sty
%doc %{_texmfdistdir}/doc/latex/filemod/README
%doc %{_texmfdistdir}/doc/latex/filemod/filemod.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
