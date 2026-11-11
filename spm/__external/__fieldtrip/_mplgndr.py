from spm._runtime import Runtime


def _mplgndr(*args, **kwargs):
    r"""
      MPLGNDR associated Legendre functions  
         
        y = mplgndr(n,k,x) computes the values of the associated Legendre  
        functions of order K up to degree N.  
          
        The input x can be a matrix, and the result is of size numel(x) by N+1.  
        The i-th column is the associated Legendre function of order K and  
        degree i-1.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/mplgndr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mplgndr", *args, **kwargs)
