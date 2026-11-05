from spm._runtime import Runtime


def _ltrisect(*args, **kwargs):
    r"""
      LTRISECT intersects a line with a plane spanned by three vertices  
         
        Use as  
          [pos] = ltrisect(v1, v2, v3, l1, l2)  
        where v1, v2 and v3 are three vertices spanning the plane, and l1 and l2  
        are two points on the line  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/ltrisect.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ltrisect", *args, **kwargs)
