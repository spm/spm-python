from spm.__wrapper__ import Runtime


def spm_nfm_mtf(*args, **kwargs):
    """
      Spectral response of a NFM (transfer function x noise spectrum)  
        FORMAT [y,w] = spm_nfm_mtf(P,M,U)  
         
        P - parameters  
        M - neural mass model structure  
        U - trial-specific effects  
         
        G - {G(N,nc,nc}} - cross-spectral density for nc channels {trials}  
                         - for N frequencies in M.Hz [default 1:64Hz]  
        w - frequencies  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_nfm_mtf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nfm_mtf", *args, **kwargs)
