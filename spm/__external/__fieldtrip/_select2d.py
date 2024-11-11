from spm.__wrapper__ import Runtime


def _select2d(*args, **kwargs):
    """
      SELECT2D helper function for selecting a rectangular region  
        in the current figure using the mouse.  
         
        Use as  
          [x, y] = select2d  
         
        It returns a 2-element vector x and a 2-element vector y   
        with the corners of the selected region.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/select2d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("select2d", *args, **kwargs)
