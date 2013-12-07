# revision 15878
# category Package
# catalog-ctan /fonts/archaic
# catalog-date 2006-11-08 11:10:08 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-archaic
Version:	20061108
Release:	6
Summary:	A collection of archaic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The collection contains fonts to represent Aramaic, Cypriot,
Etruscan, Greek of the 6th and 4th centuries BCE, Egyptian
hieroglyphics, Linear A, Linear B, Nabatean old Persian, the
Phaistos disc, Phoenician, proto-Semitic, runic, South Arabian
Ugaritic and Viking scripts. The bundle also includes a small
font for use in phonetic transcription of the archaic writings.
The bundle's own directory includes a font installation map
file for the whole collection.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/archaic/aram10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/copsn10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/cugar10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/cypr10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/etr10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/fut10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/givbc10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/gvibc10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/linb10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/nab10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/oandsi10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/oandsu10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/phnc10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/pmhg.afm
%{_texmfdistdir}/fonts/afm/public/archaic/proto10.afm
%{_texmfdistdir}/fonts/afm/public/archaic/sarab10.afm
%{_texmfdistdir}/fonts/map/dvips/archaic/aramaic.map
%{_texmfdistdir}/fonts/map/dvips/archaic/archaicprw.map
%{_texmfdistdir}/fonts/map/dvips/archaic/cypriot.map
%{_texmfdistdir}/fonts/map/dvips/archaic/etruscan.map
%{_texmfdistdir}/fonts/map/dvips/archaic/fut10.map
%{_texmfdistdir}/fonts/map/dvips/archaic/greek4cbc.map
%{_texmfdistdir}/fonts/map/dvips/archaic/greek6cbc.map
%{_texmfdistdir}/fonts/map/dvips/archaic/hieroglf.map
%{_texmfdistdir}/fonts/map/dvips/archaic/linearb.map
%{_texmfdistdir}/fonts/map/dvips/archaic/nabatean.map
%{_texmfdistdir}/fonts/map/dvips/archaic/oands.map
%{_texmfdistdir}/fonts/map/dvips/archaic/oldprsn.map
%{_texmfdistdir}/fonts/map/dvips/archaic/phoenician.map
%{_texmfdistdir}/fonts/map/dvips/archaic/protosem.map
%{_texmfdistdir}/fonts/map/dvips/archaic/sarabian.map
%{_texmfdistdir}/fonts/map/dvips/archaic/ugarite.map
%{_texmfdistdir}/fonts/source/public/archaic/copsn10.mf
%{_texmfdistdir}/fonts/source/public/archaic/givbc10.mf
%{_texmfdistdir}/fonts/source/public/archaic/gvibc10.mf
%{_texmfdistdir}/fonts/source/public/archaic/sarab10.mf
%{_texmfdistdir}/fonts/source/public/archaic/vik10.mf
%{_texmfdistdir}/fonts/source/public/archaic/vikglyph.mf
%{_texmfdistdir}/fonts/source/public/archaic/viktitle.mf
%{_texmfdistdir}/fonts/tfm/public/archaic/aram10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/copsn10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/cugar10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/cypr10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/etr10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/fut10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/givbc10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/gvibc10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/linb10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/nab10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/oandsi10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/oandsu10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/phnc10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/pmhg.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/proto10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/sarab10.tfm
%{_texmfdistdir}/fonts/tfm/public/archaic/vik10.tfm
%{_texmfdistdir}/fonts/type1/public/archaic/aram10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/copsn10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/cugar10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/cypr10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/etr10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/fut10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/givbc10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/gvibc10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/linb10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/nab10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/oandsi10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/oandsu10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/phnc10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/pmhg.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/proto10.pfb
%{_texmfdistdir}/fonts/type1/public/archaic/sarab10.pfb
%{_texmfdistdir}/tex/latex/archaic/aramaic.sty
%{_texmfdistdir}/tex/latex/archaic/cypriot.sty
%{_texmfdistdir}/tex/latex/archaic/etruscan.sty
%{_texmfdistdir}/tex/latex/archaic/greek4cbc.sty
%{_texmfdistdir}/tex/latex/archaic/greek6cbc.sty
%{_texmfdistdir}/tex/latex/archaic/hieroglf.sty
%{_texmfdistdir}/tex/latex/archaic/linearb.sty
%{_texmfdistdir}/tex/latex/archaic/nabatean.sty
%{_texmfdistdir}/tex/latex/archaic/oands.sty
%{_texmfdistdir}/tex/latex/archaic/oldprsn.sty
%{_texmfdistdir}/tex/latex/archaic/ot1aram.fd
%{_texmfdistdir}/tex/latex/archaic/ot1copsn.fd
%{_texmfdistdir}/tex/latex/archaic/ot1cugar.fd
%{_texmfdistdir}/tex/latex/archaic/ot1cypr.fd
%{_texmfdistdir}/tex/latex/archaic/ot1etr.fd
%{_texmfdistdir}/tex/latex/archaic/ot1fut.fd
%{_texmfdistdir}/tex/latex/archaic/ot1givbc.fd
%{_texmfdistdir}/tex/latex/archaic/ot1gvibc.fd
%{_texmfdistdir}/tex/latex/archaic/ot1nab.fd
%{_texmfdistdir}/tex/latex/archaic/ot1oands.fd
%{_texmfdistdir}/tex/latex/archaic/ot1phnc.fd
%{_texmfdistdir}/tex/latex/archaic/ot1pmhg.fd
%{_texmfdistdir}/tex/latex/archaic/ot1proto.fd
%{_texmfdistdir}/tex/latex/archaic/ot1sarab.fd
%{_texmfdistdir}/tex/latex/archaic/ot1vik.fd
%{_texmfdistdir}/tex/latex/archaic/phoenician.sty
%{_texmfdistdir}/tex/latex/archaic/protosem.sty
%{_texmfdistdir}/tex/latex/archaic/runic.sty
%{_texmfdistdir}/tex/latex/archaic/sarabian.sty
%{_texmfdistdir}/tex/latex/archaic/t1aram.fd
%{_texmfdistdir}/tex/latex/archaic/t1copsn.fd
%{_texmfdistdir}/tex/latex/archaic/t1cugar.fd
%{_texmfdistdir}/tex/latex/archaic/t1cypr.fd
%{_texmfdistdir}/tex/latex/archaic/t1etr.fd
%{_texmfdistdir}/tex/latex/archaic/t1fut.fd
%{_texmfdistdir}/tex/latex/archaic/t1givbc.fd
%{_texmfdistdir}/tex/latex/archaic/t1gvibc.fd
%{_texmfdistdir}/tex/latex/archaic/t1linb.fd
%{_texmfdistdir}/tex/latex/archaic/t1nab.fd
%{_texmfdistdir}/tex/latex/archaic/t1oands.fd
%{_texmfdistdir}/tex/latex/archaic/t1phnc.fd
%{_texmfdistdir}/tex/latex/archaic/t1pmhg.fd
%{_texmfdistdir}/tex/latex/archaic/t1proto.fd
%{_texmfdistdir}/tex/latex/archaic/t1sarab.fd
%{_texmfdistdir}/tex/latex/archaic/t1vik.fd
%{_texmfdistdir}/tex/latex/archaic/ugarite.sty
%{_texmfdistdir}/tex/latex/archaic/viking.sty
%doc %{_texmfdistdir}/doc/fonts/archaic/README.PRW
%doc %{_texmfdistdir}/doc/fonts/archaic/aramaic-README
%doc %{_texmfdistdir}/doc/fonts/archaic/aramaic.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/asamples.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/asamples.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/cypriot-README
%doc %{_texmfdistdir}/doc/fonts/archaic/cypriot.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/etruscan-README
%doc %{_texmfdistdir}/doc/fonts/archaic/etruscan.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/greek4cbc-README
%doc %{_texmfdistdir}/doc/fonts/archaic/greek4cbc-trygivbc.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/greek4cbc-trygivbc.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/greek4cbc.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/greek6cbc-README
%doc %{_texmfdistdir}/doc/fonts/archaic/greek6cbc-trygvibc.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/greek6cbc-trygvibc.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/greek6cbc.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/hieroglf-README
%doc %{_texmfdistdir}/doc/fonts/archaic/hieroglf-trypmhg.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/hieroglf-trypmhg.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/hieroglf.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/linearb-README
%doc %{_texmfdistdir}/doc/fonts/archaic/linearb.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/nabatean-README
%doc %{_texmfdistdir}/doc/fonts/archaic/nabatean.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/oands-README
%doc %{_texmfdistdir}/doc/fonts/archaic/oands.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/oldprsn-README
%doc %{_texmfdistdir}/doc/fonts/archaic/oldprsn.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/phoenician-README
%doc %{_texmfdistdir}/doc/fonts/archaic/phoenician-tryphnc.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/phoenician-tryphnc.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/phoenician.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/protosem-README
%doc %{_texmfdistdir}/doc/fonts/archaic/protosem.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/runic-README
%doc %{_texmfdistdir}/doc/fonts/archaic/runic.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/sarabian-README
%doc %{_texmfdistdir}/doc/fonts/archaic/sarabian.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryaramaic.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryaramaic.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/trycypriot.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/trycypriot.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryetruscan.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryetruscan.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/trylinearb.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/trylinearb.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/trynabatean.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/trynabatean.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryoands.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryoands.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryoldprsn.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryoldprsn.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryprotosem.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryprotosem.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryrunic.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryrunic.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/trysarabian.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/trysarabian.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/tryugarite.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/tryugarite.tex
%doc %{_texmfdistdir}/doc/fonts/archaic/ugarite-README
%doc %{_texmfdistdir}/doc/fonts/archaic/ugarite.pdf
%doc %{_texmfdistdir}/doc/fonts/archaic/viking-README
%doc %{_texmfdistdir}/doc/fonts/archaic/viking-try_vik.tex
#- source
%doc %{_texmfdistdir}/source/fonts/archaic/aramaic.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/aramaic.ins
%doc %{_texmfdistdir}/source/fonts/archaic/cypriot.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/cypriot.ins
%doc %{_texmfdistdir}/source/fonts/archaic/etruscan.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/etruscan.ins
%doc %{_texmfdistdir}/source/fonts/archaic/greek4cbc.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/greek4cbc.ins
%doc %{_texmfdistdir}/source/fonts/archaic/greek6cbc.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/greek6cbc.ins
%doc %{_texmfdistdir}/source/fonts/archaic/hieroglf.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/hieroglf.ins
%doc %{_texmfdistdir}/source/fonts/archaic/linearb.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/linearb.ins
%doc %{_texmfdistdir}/source/fonts/archaic/nabatean.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/nabatean.ins
%doc %{_texmfdistdir}/source/fonts/archaic/oands.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/oands.ins
%doc %{_texmfdistdir}/source/fonts/archaic/oldprsn.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/oldprsn.ins
%doc %{_texmfdistdir}/source/fonts/archaic/phoenician.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/phoenician.ins
%doc %{_texmfdistdir}/source/fonts/archaic/protosem.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/protosem.ins
%doc %{_texmfdistdir}/source/fonts/archaic/runic.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/runic.ins
%doc %{_texmfdistdir}/source/fonts/archaic/sarabian.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/sarabian.ins
%doc %{_texmfdistdir}/source/fonts/archaic/ugarite.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/ugarite.ins
%doc %{_texmfdistdir}/source/fonts/archaic/viking.dtx
%doc %{_texmfdistdir}/source/fonts/archaic/viking.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061108-2
+ Revision: 749343
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061108-1
+ Revision: 717850
- texlive-archaic
- texlive-archaic
- texlive-archaic
- texlive-archaic
- texlive-archaic

