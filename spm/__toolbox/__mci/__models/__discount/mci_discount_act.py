from spm._runtime import Runtime


def mci_discount_act(*args, **kwargs):
    r"""
      Activation of discounting model  
        FORMAT [a,v1,v2,k] = mci_discount_act (P,M,U)  
         
        P         parameters  
        M         model structure  
        U         contains rewards and times  
         
        a         activation for discount model  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/discount/mci_discount_act.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_act", *args, **kwargs)
