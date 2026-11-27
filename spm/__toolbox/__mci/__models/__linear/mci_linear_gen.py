from spm._runtime import Runtime


def mci_linear_gen(*args, **kwargs):
    r"""
      Output of linear model  
        FORMAT [y] = mci_linear_gen (theta,M,U)  
         
        theta     regression coefficients  
        M         model structure  
        U         U.X contains design matrix  
         
        y         outputs  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/linear/mci_linear_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linear_gen", *args, **kwargs)
