from spm._runtime import Runtime


def mci_logistic_act(*args, **kwargs):
    r"""
      Activations of logistic model  
        FORMAT [a] = mci_logistic_act (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         contains rewards and times  
         
        a         activations of logistic model  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/logistic/mci_logistic_act.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_logistic_act", *args, **kwargs)
