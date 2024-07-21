# DecryptZero

## Introduction
DecryptZero is a **fully open-source** OCR (Optical Character Recognition) model for chess tournament notation sheets. DecryptZero runs on a model trained specifically to read chess players' handwriting (which can get very messy at times!) through the open-source [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) repository (the [decrypt-trainer](decrypt-trainer) directory in this repo).

## Current State
The engine has completed training. It runs with superb accuracy on single-word images but is not yet compatible with the algorithms to read full notation sheets. Image preprocessing algorithms are complete, but they may be overhauled in the future for more efficient and accurate results.

## What's Next?
Integrate the engine with `ocr-easy.py` to test on full notation-sheets rather than one-word samples.

## Usage
Clone the repository with `git clone https://codeberg.org/KPLinux/DecryptZero`. The main file is [ocr-easy.py](ocr-easy.py); however, since the engine is still in integration phase, it is likely not to function (yet). Fix will come out soon.

Currently, the only way to run the program is through the command line interface. A graphical user interface may come in the future.

To use the OCR (through the CLI), you will need to pass 3 arguments:
* `--image` - the path to the image you would like to OCR
* `--align-template` - the path to the template that the image will be aligned with during preprocessing
* `--box-template` - the path to the template that will create the bounding boxes where OCR will be performed

There are currently two template options because the alignment algorithm looks for key points on the image to be mapped to the template (which must be a carbon copy of the image) and the boxing algorithm looks for grid lines on the template (which requires a preprocessed image that has the gridlines enhanced to be darker). Because the nature of these templates are fundamentally different, the arguments cannot (yet) be combined into a single `--template` argument.

## Potential Improvements
It would be more efficient if an alignment template/algorithm wasn't necessary to produce accurate results. In the future, an attempt will be made to create a general program that deals with all the intricacies of the sheet in one single scan.