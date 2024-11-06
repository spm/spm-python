from spm.__wrapper__ import Runtime


def mci_discount_gen(*args, **kwargs):
    """
      Output of discounting model  
        FORMAT [g,y] = mci_discount_gen (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         U.X contains design matrix  
         
        g         probability of taking option 1  
        y         binary decisions based on g  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_discount_gen", *args, **kwargs)
