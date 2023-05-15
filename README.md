# CSE150-UCSC
Published: No

Backblaze: Yes

Github: Yes

Google Drive: Yes

## Info

- Github does not properly render markdown and TeX on some files.
- Chapter 1-3 slides: https://nbviewer.org/github/bunfloof/CSE150-UCSC/blob/main/CSE150%20Chap1-3%20OCR%20Orientation-fixed.pdf
- PDF Sample Midterm: https://nbviewer.org/github/bunfloof/CSE150-UCSC/tree/main/Sample%20Midterm%20f5398307c41a4a95b7db2012011e2da5.pdf
## How to compile everything

Use predefined pipelines. Maybe `bun-beautiful3` ❤️

## How to compile PDFs

Convert markdown files to PDF.
### Pandoc example usage
```
pandoc -s --pdf-engine=xelatex "Lab 1_ Installing and Using Mininet-1 742a3b0d8eac40a79905934f36cd5cc1.md" -o lab1_compiled.pdf --highlight-style tango -H layout.tex
```

## How to compile READMEs

Remember to set environmental variables before compiling.
