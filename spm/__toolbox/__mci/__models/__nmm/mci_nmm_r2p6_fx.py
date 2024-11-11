from spm.__wrapper__ import Runtime


def mci_nmm_r2p6_fx(*args, **kwargs):
    """
      Flow for two region, six parameter NMM  
        FORMAT [f] = mci_nmm_r2p6_fx (x,u,P,M)  
         
        x         State  
        u         Inputs  
        P         Parameters  
        M         Model structure  
         
        f         Flow, dx/dt  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_r2p6_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_r2p6_fx", *args, **kwargs)
