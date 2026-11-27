from spm._runtime import Runtime


def spm_cond_units(*args, **kwargs):
    r"""
      Scale numeric arrays by a multiple of 10^n to avoid numerical overflow  
        FORMAT [y,scale] = spm_cond_units(y,n)  
          y - y*scale;  
          n - default 3  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cond_units.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cond_units", *args, **kwargs)
