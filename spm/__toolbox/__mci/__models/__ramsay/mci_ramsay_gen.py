from spm._runtime import Runtime


def mci_ramsay_gen(*args, **kwargs):
    r"""
      Generate data from Ramsay model  
        FORMAT [Y] = mci_ramsay_gen (P,M,U)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
         
        Y         Data  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/ramsay/mci_ramsay_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_ramsay_gen", *args, **kwargs)
