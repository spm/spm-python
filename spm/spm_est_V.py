from spm._runtime import Runtime


def spm_est_V(*args, **kwargs):
    r"""
      Test routine to evaluate non-sphericity correction (ReML Whitening)  
        FORMAT [h] = spm_est_V(SPM,c)  
        SPM    - structure containing generic analysis details  
        c      - number of contrasts to simulate (default = 4)  
         
        h      - hyperparameter estimates  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_est_V.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_est_V", *args, **kwargs)
