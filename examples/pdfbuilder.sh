#!/usr/bin/env bash
../tikzbuild mux2.json
pdflatex mux2.tex
rm -f *.aus *.log
