from spm._runtime import Runtime


def spm_nfm_mtf(*args, **kwargs):
    r"""
      Spectral response of a NFM (transfer function x noise spectrum)  
        FORMAT [y,w] = spm_nfm_mtf(P,M,U)  
         
        P - parameters  
        M - neural mass model structure  
        U - trial-specific effects  
         
        G - {G(N,nc,nc}} - cross-spectral density for nc channels {trials}  
                         - for N frequencies in M.Hz [default 1:64Hz]  
        w - frequencies  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_nfm_mtf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_nfm_mtf", *args, **kwargs)
