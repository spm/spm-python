from spm._runtime import Runtime


def _cdat2rgb(*args, **kwargs):
    r"""
      This function changes the color of pixels to white, regardless of colormap, without using opengl  
        It does by converting by:  
        1) convert the to-be-plotted data to their respective rgb color values (determined by colormap)  
        2) convert these rgb color values to hsv values, hue-saturation-value  
        3) for to-be-masked-pixels, set saturation to 0 and value to 1 (hue is irrelevant when they are)  
        4) convert the hsv values back to rgb values  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/cdat2rgb.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cdat2rgb", *args, **kwargs)
