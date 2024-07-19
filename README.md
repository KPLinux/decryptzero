# DecryptZero

## Introduction
DecryptZero is a **fully open-source** OCR (Optical Character Recognition) model for chess tournament notation sheets. DecryptZero runs on a model trained specifically to read chess players' handwriting (which can get very messy at times!) through the open-source [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) repo.

## Installation
Clone the repository with `git clone https://codeberg.org/KPLinux/DecryptZero`. The main file is [ocr-easy.py](ocr-easy.py).

To use `ocr.py`, you will need to pass 3 arguments:
`--image` - the path to the image you would like to OCR
`--align-template` - the path to the template that the image will be aligned with during preprocessing
`--box-template` - the path to the template that will create the bounding boxes where OCR will be performed