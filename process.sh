#!/bin/sh

#
#	Convert all of my pdfs downloaded from chase.com to pdf
#	brew install xpdf
#
for f in *.pdf; do 
	pdftotext -layout $f
done