from spm._runtime import Runtime


def _plgndr(*args, **kwargs):
    """
      PLGNDR associated Legendre function  
         
        y = plgndr(n,k,x) computes the values of the associated Legendre functions  
        of degree N and order K  
         
        implemented as MEX file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/plgndr.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("plgndr", *args, **kwargs)
