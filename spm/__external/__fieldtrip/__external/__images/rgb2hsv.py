from spm.__wrapper__ import Runtime


def rgb2hsv(*args, **kwargs):
    """
      RGB2HSV converts red-green-blue colors to hue-saturation-value.  
         
        this code is based on the comments in  
        http://stackoverflow.com/questions/3018313/algorithm-to-convert-rgb-to-hsv-and-hsv-to-rgb-in-range-0-255-for-both  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/images/rgb2hsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rgb2hsv", *args, **kwargs)
