from spm._runtime import Runtime


def _brain(*args, **kwargs):
    """
      returns a predefined color as [red green blue] values  
         
        skin_surface         = [255 213 119]/255;  
        outer_skull_surface  = [140  85  85]/255;  
        inner_skull_surface  = [202 100 100]/255;  
        cortex = [255 213 119]/255;  
        black  = [0   0   0  ]/255;  
        white  = [255 255 255]/255;  
        red    = [255 0   0  ]/255;  
        green  = [0   192 0  ]/255;  
        blue   = [0   0   255]/255;  
        yellow = [255 255 0  ]/255;  
        cortex_light = [199 194 169]/255;  
        cortex_dark  = [100 97 85]/255;  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/brain.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("brain", *args, **kwargs)
