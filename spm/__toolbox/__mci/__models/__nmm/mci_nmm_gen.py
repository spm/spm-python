from spm._runtime import Runtime


def mci_nmm_gen(*args, **kwargs):
    r"""
      Generate data from two region NMM   
        FORMAT [Y] = mci_nmm_gen (M,U,P)  
         
        M         Model structure  
        U         Inputs  
        P         Parameters  
         
        Y         Data  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/nmm/mci_nmm_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_nmm_gen", *args, **kwargs)
