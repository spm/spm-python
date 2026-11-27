from spm._runtime import Runtime


def mci_ramsay_struct(*args, **kwargs):
    r"""
      Data structures for Ramsay model  
        FORMAT [M,U] = mci_ramsay_struct (sigme_e)  
         
        sigma_e       Noise SD  
         
        M,U           model, input data structures  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/ramsay/mci_ramsay_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_ramsay_struct", *args, **kwargs)
