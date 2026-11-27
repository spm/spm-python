from spm._runtime import Runtime


def _tritrisect(*args, **kwargs):
    r"""
      TRITRISECT computes the intersection line of a triangle with a plane  
        spanned by three vertices v1, v2 and v3.  
         
        [l1, l2] = tritrisect(v1, v2, v3, t1, t2, t3)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/tritrisect.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tritrisect", *args, **kwargs)
