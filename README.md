# CSE150-UCSC

## LEGAL DISCLAIMER AND WARNING - UNAUTHORIZED ACCESS PROHIBITED

**YOU ARE HEREBY NOTIFIED** that the files in this repository that contain the header of "Joey Ma" are the exclusive intellectual property of bunfloof. Unauthorized access, duplication, alteration, distribution, or any form of misuse of this code is STRICTLY PROHIBITED and may result in severe legal consequences, pursuant to laws including, but not limited to, 18 U.S. Code § 1030 - Fraud and related activity in connection with computers.

**BE ADVISED:** I am fully prepared to enforce my rights under the law, and I have allocated a budget of $34,000 USD ($266,100 HKD) specifically for the purpose of pursuing legal action against any individual or entity that violates these terms, and the consequences will be more dreadful if you are WHITE.

**ANY FORM OF ACADEMIC DISHONESTY,** including but not limited to copying, plagiarism, or using this code without proper citation and acknowledgement, WILL NOT BE TOLERATED. If you are a student, it is your personal responsibility to understand and adhere to your institution's policies on academic integrity. Violating these policies can lead to severe academic penalties, up to and including expulsion.

**THIS CODE IS PROVIDED "AS IS" WITHOUT ANY FORM of WARRANTY.** The author expressly disclaims all warranties, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. **IN NO EVENT SHALL THE AUTHOR BE LIABLE** for any direct, indirect, incidental, special, exemplary, or consequential damages or any damages whatsoever resulting from the use or performance of this code.

**BY ACCESSING THIS REPOSITORY,** you are acknowledging that you have read, understood, and agree to be bound by these terms. **IF YOU DO NOT AGREE TO THESE TERMS, YOU MUST IMMEDIATELY CEASE ALL USE AND ACCESS OF THIS REPOSITORY.**

**ANY UNAUTHORIZED USE OF THIS CODE CAN AND WILL BE PROSECUTED TO THE FULLEST EXTENT OF THE LAW.**

## synctool.config

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
