from spm._runtime import Runtime


def mci_discount_struct(*args, **kwargs):
    r"""
      Set up data structures for discounting model  
        FORMAT [M,U] = mci_discount_struct (Nobs)  
         
        Nobs      number of data points  
         
        M         model structure  
        U         U.X is the design matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/discount/mci_discount_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_struct", *args, **kwargs)
