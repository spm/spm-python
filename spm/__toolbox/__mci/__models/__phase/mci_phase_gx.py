from spm._runtime import Runtime


def mci_phase_gx(*args, **kwargs):
    r"""
      Observation function for phase model  
        FORMAT [y,L] = mci_phase_gx (x,u,P,M)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_phase_gx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_gx", *args, **kwargs)
