from spm._runtime import Runtime


def mci_lds_gx(*args, **kwargs):
    r"""
      Observation function for LDS  
        FORMAT [y,L] = mci_lds_gx (x,u,P,M)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/lds/mci_lds_gx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_gx", *args, **kwargs)
