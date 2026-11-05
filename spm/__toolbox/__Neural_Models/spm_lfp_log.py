from spm._runtime import Runtime


def spm_lfp_log(*args, **kwargs):
    r"""
      Feature selection for lfp and mtf (spectral) neural mass models  
        FORMAT [y] = spm_lfp_log(y,M)  
          
        Y -> log(y) (including cells)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_lfp_log.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lfp_log", *args, **kwargs)
