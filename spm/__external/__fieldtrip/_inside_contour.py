from spm.__wrapper__ import Runtime


def _inside_contour(*args, **kwargs):
    """
    inside_contour is a function.  
          bool = inside_contour(pos, contour)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/inside_contour.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("inside_contour", *args, **kwargs)
