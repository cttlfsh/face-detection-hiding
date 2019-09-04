# Face Detection and Hiding

A simple algorithm for face detection which also allows the user to automatically hide the detected faces. Moreover, in the case the detection missed some face, those can be manually selected and obscured.

At the moment the implemented hiding methods are four:
  - *Blur*
  - *Pixel Shuffle*
  - *Image Swap*
  - *Negative*

## 1] Requirements
In order to be able to run the software, there are some requirements:
  - OpenCV-Python: which can be installed with the command `pip3 install opencv-python`
  - The OpenCV contrib modules (not mandatory): `pip3 install opencv-contrib-python`
  - Numpy, which should be automatically installed with OpenCV

## 2] Run

There are two version of the software, one very basic, another a little more advanced.
  - The **simple** version consist in a script which can be run with:
  
        `python3 face_detection.py`

    and it just loads a fixed image, detect faces in it and hides them. The only way to
    control the hiding method is via uncommenting code lines.

  - The '**advanced**' version of the software introduces concepts of classes, methods
  and command line arguments. The script can be run with:

        `python3 face_detection_adv.py` -f [filename] -p [True|False] -m [blur|shuffle|negative|image_swap] 

  The parameters are one for the image path to use (*-f* ), one for deciding if the privacy mode should be active or not (*-p* ), when the privacy mode is active then the faces will be obscured. The hiding method can be selected with the option *-m*. If the option is not set and the privacy mode is active, default method is *blur* .
  
### 3] Python + Images useful material

Here there is a list of references which can be useful to start working with Python and Images:

  - [PyImageSearch](https://www.pyimagesearch.com/)
  - [CodeCombat](https://codecombat.com) 
  - [Repl](https://repl.it/languages/python3)
  - [Python Imaging Library Handbook](http://effbot.org/imagingbook/pil-index.htm)
  - [Hands on Image Processing](https://www.researchgate.net/profile/Sandipan_Dey/publication/329610370_Hands-on_Image_Processing_in_Python/links/5c120f09299bf139c754a03c/Hands-on-Image-Processing-in-Python.pdf)
