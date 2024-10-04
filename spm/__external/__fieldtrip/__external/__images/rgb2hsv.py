from spm.__wrap__ import _Runtime


def rgb2hsv(*args, **kwargs):
  """  RGB2HSV converts red-green-blue colors to hue-saturation-value.  
     
    this code is based on the comments in  
    http://stackoverflow.com/questions/3018313/algorithm-to-convert-rgb-to-hsv-and-hsv-to-rgb-in-range-0-255-for-both  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/images/rgb2hsv.m)
  """

  return _Runtime.call("rgb2hsv", *args, **kwargs)
