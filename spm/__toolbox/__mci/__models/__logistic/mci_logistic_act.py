from spm.__wrapper__ import Runtime


def mci_logistic_act(*args, **kwargs):
    """
      Activations of logistic model  
        FORMAT [a] = mci_logistic_act (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         contains rewards and times  
         
        a         activations of logistic model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_act.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_logistic_act", *args, **kwargs)
