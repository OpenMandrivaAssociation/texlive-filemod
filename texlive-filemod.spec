%global tl_name filemod
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Provide file modification times, and compare them
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filemod
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filemod.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filemod.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros to read and compare the modification dates
of files. The files may be .tex files, images or other files (as long as
they can be found by LaTeX). It uses the \pdffilemoddate primitive of
pdfLaTeX to find the file modification date as PDF date string, parses
the string and returns the value to the user. The package will also work
for DVI output with recent versions of the LaTeX compiler which uses
pdfLaTeX in DVI mode. The functionality is provided by purely expandable
macros or by faster but non-expandable ones.

