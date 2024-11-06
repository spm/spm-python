from spm.__wrapper__ import Runtime


def spm_mci_ess(*args, **kwargs):
    """
      Compute Effective Sample Size  
        FORMAT [ess,m] = spm_mci_ess (x,p)  
         
        x      Univariate time series  
        p      Maximum lag for autocovariance estimation  
         
        ess    Effective Sample Size  
        m      Number of lags used in ESS estimate  
         
        This routine is based on the Initial Positive Sequence estimate  
        proposed in C. Geyer (1992) Practical Markov Chain Monte Carlo,   
        Statistical Science, 7(4):473-511.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_ess.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_ess", *args, **kwargs)
