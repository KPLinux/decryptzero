# DecryptZero

## Introduction
DecryptZero is a **fully open-source** OCR (Optical Character Recognition) model for chess tournament notation sheets. DecryptZero runs on a model trained specifically to read chess players' handwriting (which can get very messy at times!) through the open-source [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) repo.

## Current State
The engine is still in the training/testing phase. Image preprocessing algorithms are complete, but they may be overhauled in the future for more efficient and accurate results.

## What's Next?
Continue training the engine. When complete, integrate it with `ocr-easy.py` to test on full notation-sheets rather than one word samples.

## Usage
Clone the repository with `git clone https://codeberg.org/KPLinux/DecryptZero`. The main file is [ocr-easy.py](ocr-easy.py); however, since the engine is still in training phase, it is better to use [ocr-tess.py](ocr.tess.py) (untrained) for demonstration purposes.

To use the OCR, you will need to pass 3 arguments:
* `--image` - the path to the image you would like to OCR
* `--align-template` - the path to the template that the image will be aligned with during preprocessing
* `--box-template` - the path to the template that will create the bounding boxes where OCR will be performed

There are currently two template options because the alignment algorithm looks for key points on the image to be mapped to the template (which must be a carbon copy of the image) and the boxing algorithm looks for grid lines on the template (which requires a preprocessed image that has the gridlines enhanced to be darker). Because the nature of these templates are fundamentally different, the arguments cannot (yet) be combined into a single `--template` argument.