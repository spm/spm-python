from spm._runtime import Runtime


def plgndr(*args, **kwargs):
    r"""
      PLGNDR computes the values of the associated Legendre functions  
        of degree N and order K  
         
        Use as  
          y = plgndr(n,k,x)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/plgndr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("plgndr", *args, **kwargs)
