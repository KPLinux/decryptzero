# DecryptZero

## Introduction
DecryptZero is a **fully open-source** OCR (Optical Character Recognition) model for chess tournament notation sheets. DecryptZero runs on a model trained specifically to read chess players' handwriting (which can get very messy at times!) through the open-source [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) repository (the [decrypt-trainer](decrypt-trainer) directory in this repo).

## Current State
The engine has completed training. It runs with superb accuracy on the training and testing sets but is not yet compatible with the algorithms to read full notation sheets. Image preprocessing algorithms are complete, but they may be overhauled in the future for more efficient and accurate results.

## What's Next?
Integrate the engine with `ocr-easy.py` to test on full notation-sheets rather than one-word samples.

## Usage

### Prerequisites
If you have an NVIDIA GPU that is CUDA capable, you can install CUDA by following the instructions for your operating system and distribution [here](https://docs.nvidia.com/cuda/index.html). The programs will run much faster on GPU but can still run perfectly fine on CPU. You can check if your NVIDIA GPU is CUDA capable [here](https://developer.nvidia.com/cuda-gpus).

### Dependencies
The three main libraries needed to run the programs are **OpenCV**, **EasyOCR**, and **boxdetect**. OpenCV is a library used for processing images before an OCR model reads them so the results are more accurate. EasyOCR is the model itself, and boxdetect is used to find and create bounding boxes around the text, which creates regions of interest (ROIs) that will be read by the OCR engine.

#### Main
You can install OpenCV with `apt` or as a `pip` package *(recommended)*:
```
sudo apt-get install python3 opencv
```
```
pip install opencv-python
```

You can install EasyOCR and boxdetect as `pip` packages:
```
pip install easyocr
```
```
pip install boxdetect
```

#### Other
Since the program is run in the command line with custom arguments, you will need to install `argparse` (if it is not already installed):
```
pip install argparse
```

You will need to install `imutils`, which is used for resizing the output to be visualized properly:
```
pip install imutils
```

You will also need to install `numpy` for proper conversion of data types and `matplotlib` to visualize results:
```
pip install numpy
```
```
pip install matplotlib
```

### Running the Program
Clone the repository with `git clone https://codeberg.org/KPLinux/DecryptZero`. The main file is [ocr-easy.py](ocr-easy.py).

The model files are too large to be pushed to the repository, so they are linked in a Google Drive [here](https://drive.google.com/drive/u/0/folders/1GTqZIXgyWEjPCoaXjRuHV2CLwYTYAeSv) instead.

Currently, the only way to run the program is through the command line interface. A graphical user interface may come in the future.

To use the OCR (through the CLI), you will need to pass 3 arguments:
* `--image` - the path to the image you would like to OCR
* `--align-template` - the path to the template that the image will be aligned with during preprocessing
* `--box-template` - the path to the template that will create the bounding boxes where OCR will be performed

Make sure you are in the `ocr/` directory.

Paste this line to run on the sample image & templates:

```
python3 ocr-easy.py --image sample/image.png --align-template sample/align-template.png --box-template sample/box-template.png
```

The output will be the input image and a carbon copy of that image with bounding boxes and the detected text in each bounding box.

There are currently two template options because the alignment algorithm looks for key points on the image to be mapped to the template (which must be a carbon copy of the image) and the boxing algorithm looks for grid lines on the template (which requires a preprocessed image that has the gridlines enhanced to be darker). Because the nature of these templates are fundamentally different, the arguments cannot (yet) be combined into a single `--template` argument.

## Potential Improvements
It would be more efficient if an alignment template/algorithm wasn't necessary to produce accurate results. In the future, an attempt will be made to create a general program that deals with all the intricacies of the sheet in one single scan.