from spm.__wrapper__ import Runtime


def mci_linear_gen(*args, **kwargs):
    """
      Output of linear model  
        FORMAT [y] = mci_linear_gen (theta,M,U)  
         
        theta     regression coefficients  
        M         model structure  
        U         U.X contains design matrix  
         
        y         outputs  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_linear_gen", *args, **kwargs)
