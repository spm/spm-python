from spm.__wrapper__ import Runtime


def mci_lds_gx(*args, **kwargs):
    """
      Observation function for LDS  
        FORMAT [y,L] = mci_lds_gx (x,u,P,M)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_gx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_gx", *args, **kwargs)
