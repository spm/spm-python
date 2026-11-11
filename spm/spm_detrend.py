from spm._runtime import Runtime


def spm_detrend(*args, **kwargs):
    r"""
      Polynomial detrending over columns  
        FORMAT y = spm_detrend(x,p)  
        x   - data matrix  
        p   - order of polynomial [default: 0]  
          
        y   - detrended data matrix  
       __________________________________________________________________________  
         
        spm_detrend removes linear and nonlinear trends from column-wise data  
        matrices.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_detrend.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_detrend", *args, **kwargs)
