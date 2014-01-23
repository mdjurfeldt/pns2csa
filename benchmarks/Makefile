all:
	python plot_bench.py
	inkscape --export-pdf=CSAConnector_.pdf CSAConnector.svg
	pdfcrop CSAConnector_.pdf CSAConnector.pdf
	inkscape --export-pdf=native_routines_.pdf native_routines.svg
	pdfcrop native_routines_.pdf native_routines.pdf
