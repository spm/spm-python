from spm._runtime import Runtime


def _select2d(*args, **kwargs):
    r"""
      SELECT2D helper function for selecting a rectangular region  
        in the current figure using the mouse.  
         
        Use as  
          [x, y] = select2d  
         
        It returns a 2-element vector x and a 2-element vector y   
        with the corners of the selected region.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/select2d.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("select2d", *args, **kwargs)
