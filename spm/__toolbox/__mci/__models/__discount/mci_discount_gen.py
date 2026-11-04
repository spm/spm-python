from spm._runtime import Runtime


def mci_discount_gen(*args, **kwargs):
    r"""
      Output of discounting model  
        FORMAT [g,y] = mci_discount_gen (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         U.X contains design matrix  
         
        g         probability of taking option 1  
        y         binary decisions based on g  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/discount/mci_discount_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_gen", *args, **kwargs)
