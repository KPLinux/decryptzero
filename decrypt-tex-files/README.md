# Presentation Materials

## Prerequisites
To compile the source code into readable PDF files, you have to run the `pdflatex` command. To be able to use it, install `texlive`:

```shell
sudo apt install texlive-latex-recommended texlive-latex-extra
```

## Compiling
It is recommended to create separate directories for each document, since the compilation will create new files which are best grouped together.

Run the following commands (separately) to compile each document:

```shell
pdflatex algorithms.tex
```

```shell
pdflatex decrypt-paper.tex
```

```shell
pdflatex decrypt-slides.tex
```