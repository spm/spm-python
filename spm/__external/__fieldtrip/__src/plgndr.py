from spm.__wrapper__ import Runtime


def plgndr(*args, **kwargs):
    """
      PLGNDR associated Legendre function  
         
        y = plgndr(n,k,x) computes the values of the associated Legendre functions  
        of degree N and order K  
         
        implemented as MEX file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/plgndr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("plgndr", *args, **kwargs)
