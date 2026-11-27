from spm._runtime import Runtime


def spm_interp(*args, **kwargs):
    r"""
      1 or 2-D array interpolation  
        FORMAT [x] = spm_interp(x,r)  
        x - array  
        r - interpolation rate  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_interp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_interp", *args, **kwargs)
