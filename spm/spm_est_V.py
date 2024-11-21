from spm.__wrapper__ import Runtime


def spm_est_V(*args, **kwargs):
    """
      Test routine to evaluate non-sphericity correction (ReML Whitening)  
        FORMAT [h] = spm_est_V(SPM,c)  
        SPM    - structure containing generic analysis details  
        c      - number of contrasts to simulate (default = 4)  
         
        h      - hyperparameter estimates  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_est_V.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_est_V", *args, **kwargs)
