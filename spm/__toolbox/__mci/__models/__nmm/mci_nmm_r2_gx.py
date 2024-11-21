from spm.__wrapper__ import Runtime


def mci_nmm_r2_gx(*args, **kwargs):
    """
      Observation function for 2-region NMM  
        FORMAT [y,L] = mci_nmm_r2_gx (x,u,P,M)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
         
        y         Output  
        L         Lead field (dy/dx)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_r2_gx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_r2_gx", *args, **kwargs)
