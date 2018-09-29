#!/usr/bin/env python
from PIL import Image
import os


  # now looping all images in your current image directory
  #(dot)to specify current directory
 for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        # fn ---file name fext ---file extension
        fn, fext = os.path.splitext(f)
        # jpegs is where we want to put output images in the format of our choice
        i.save('jpegs/{}.png'.format(fn))

