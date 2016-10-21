proposal:
	latexmk -cd -f -pdf -pdflatex='pdflatex -interaction=batchmode' -synctex=1 proposal.tex
pvc:
	latexmk -cd -f -pdf  -synctex=1 proposal.tex -pvc
clean: 
	rm -rf proposal.pdf aux  *.bbl *.blg *.log .Z* auto *.fls *.fdb_latexmk *.synctex.gz 


