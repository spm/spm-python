from spm._runtime import Runtime


def spm_spy(*args, **kwargs):
    r"""
      Pretty version of spy  
        FORMAT spm_spy(X,Markersize,m)  
        X    - sparse {m x n} matrix  
         
        See also: spy  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_spy.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_spy", *args, **kwargs, nargout=0)
