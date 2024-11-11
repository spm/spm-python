from spm.__wrapper__ import Runtime


def spm_mvb_bmc(*args, **kwargs):
    """
      Multivariate Bayesian model comparison (Baysian decoding of a contrast)  
        FORMAT [F,P,MVB] = spm_mvb_bmc(mvb)  
         
        mvb   : models to compare (file names)  
        F     : F ratio relative to null  
        P     : P-value relative to null  
        MVB   : best model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_bmc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_bmc", *args, **kwargs)
