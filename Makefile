# Makefile for latex documents

FILE=pns2csa13
BIBPATH=$(HOME)/work/bibliography/

all:
	pdflatex $(FILE)
	if test $(USERNAME) = "jochen"; then \
	  rm $(FILE)_gen.bib; \
          bibtool -x $(FILE).aux -o $(FILE)_gen.bib  $(FILE).bib\
          $(BIBPATH)brain.bib $(BIBPATH)computer.bib $(BIBPATH)math.bib;\
        fi
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)

clean:
	rm -rf *~ *.log *.aux *.bbl *.blg *.idx *.ilg *.ind *.lof *.out *.pfg *.toc

mrproper: clean
	rm -rf *.pdf *.ps *.dvi 
