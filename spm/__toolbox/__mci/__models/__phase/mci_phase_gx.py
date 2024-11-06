from spm.__wrapper__ import Runtime


def mci_phase_gx(*args, **kwargs):
    """
      Observation function for phase model  
        FORMAT [y,L] = mci_phase_gx (x,u,P,M)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_gx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_phase_gx", *args, **kwargs)
