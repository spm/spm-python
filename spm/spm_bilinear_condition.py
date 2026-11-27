from spm._runtime import Runtime


def spm_bilinear_condition(*args, **kwargs):
    r"""
      Condition a bilinear operator by suppressing positive eigenmodes  
        FORMAT M0 = spm_bilinear_condition(M0)  
        M0 - bilinear operator  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bilinear_condition.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bilinear_condition", *args, **kwargs)
