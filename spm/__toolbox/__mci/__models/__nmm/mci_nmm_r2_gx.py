from spm._runtime import Runtime


def mci_nmm_r2_gx(*args, **kwargs):
    r"""
      Observation function for 2-region NMM  
        FORMAT [y,L] = mci_nmm_r2_gx (x,u,P,M)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
         
        y         Output  
        L         Lead field (dy/dx)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/nmm/mci_nmm_r2_gx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_nmm_r2_gx", *args, **kwargs)
