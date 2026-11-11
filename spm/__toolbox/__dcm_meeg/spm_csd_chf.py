from spm._runtime import Runtime


def spm_csd_chf(*args, **kwargs):
    r"""
      Characteristic (expected) frequency of a NMM  
        FORMAT [G,w] = spm_csd_chf(P,M,U)  
         
        P - parameters  
        M - neural mass model structure  
        U - trial-specific effects  
         
        m - expected frequency  
        v - dispersion  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_csd_chf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_csd_chf", *args, **kwargs)
