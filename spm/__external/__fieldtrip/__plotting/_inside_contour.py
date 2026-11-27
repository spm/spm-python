from spm._runtime import Runtime


def _inside_contour(*args, **kwargs):
    r"""
    inside_contour is a function.  
          bool = inside_contour(pos, contour)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/inside_contour.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("inside_contour", *args, **kwargs)
