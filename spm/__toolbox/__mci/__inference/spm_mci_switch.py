from spm.__wrapper__ import Runtime


def spm_mci_switch(*args, **kwargs):
    """
      Return log probability of tempered model switch  
        FORMAT [logp,logq1,logq2] = spm_mci_switch (Pr,M,U,Y,beta)  
         
        Pr        parameters (vectorised and in M.V subspace)  
        M,U,Y     as usual  
        beta      inverse temperature (set to 1 to get usual posterior)  
         
        logp      log prob of model switch  
        logq1     log joint of model 1  
        logq2     log joint of model 2  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_switch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_switch", *args, **kwargs)
