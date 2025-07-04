from spm._runtime import Runtime


def mci_logistic_gen(*args, **kwargs):
    """
      Output of logistic regression model  
        FORMAT [g,y] = mci_logistic_gen (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         U.X contains design matrix  
         
        g         probabilities of y=1  
        y         binary decisions based on g  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_gen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_logistic_gen", *args, **kwargs)
