from spm.__wrapper__ import Runtime


def spm_mci_joint(*args, **kwargs):
    """
      Compute log joint probability of model  
        FORMAT [L,L2,st] = spm_mci_joint (Pr,M,U,Y,beta)  
         
        Pr    parameters (vectorised and in M.V subspace)  
        M     model structure  
        U     inputs  
        Y     data  
        beta  inverse temperature  
         
        L     beta * log p(Y|P) + log p(P)  
        L2    log p(Y|P)  
        st    status flag (0 for OK, -1 for problem)  
         
        A default beta=1 gives usual log joint  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_joint.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_joint", *args, **kwargs)
