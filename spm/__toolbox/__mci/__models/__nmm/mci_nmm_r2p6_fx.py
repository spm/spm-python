from spm._runtime import Runtime


def mci_nmm_r2p6_fx(*args, **kwargs):
    r"""
      Flow for two region, six parameter NMM  
        FORMAT [f] = mci_nmm_r2p6_fx (x,u,P,M)  
         
        x         State  
        u         Inputs  
        P         Parameters  
        M         Model structure  
         
        f         Flow, dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/nmm/mci_nmm_r2p6_fx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_nmm_r2p6_fx", *args, **kwargs)
