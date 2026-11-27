from spm._runtime import Runtime


def spm_fp_display_nullclines(*args, **kwargs):
    r"""
      Nullcline plot of flow and sample trajectory  
        FORMAT spm_fp_display_nullclines(M,x)  
         
        M   - model specifying flow; M(1).f;  
        x   - cell array of domain or support  
         
        f   - derivative of x(2)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fp_display_nullclines.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fp_display_nullclines", *args, **kwargs)
