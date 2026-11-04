from spm._runtime import Runtime


def spm_cross(*args, **kwargs):
    r"""
      Multidimensional cross (outer) product  
        FORMAT [Y] = spm_cross(X,x,...)  
        FORMAT [Y] = spm_cross(X)  
         
        X  - cell or numeric array  
        x  - cell or numeric array  
         
        Y  - outer product  
         
        See also: spm_dot  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cross.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cross", *args, **kwargs)
