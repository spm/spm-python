from spm.__wrapper__ import Runtime


def _tritrisect(*args, **kwargs):
    """
      TRITRISECT computes the intersection line of a triangle with a plane  
        spanned by three vertices v1, v2 and v3.  
         
        [l1, l2] = tritrisect(v1, v2, v3, t1, t2, t3)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/tritrisect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tritrisect", *args, **kwargs)
