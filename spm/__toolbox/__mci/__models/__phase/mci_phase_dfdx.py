from spm._runtime import Runtime


def mci_phase_dfdx(*args, **kwargs):
    r"""
      State sensitivity for phase model  
        FORMAT [dfdx] = mci_phase_dfdx (x,u,P,M)  
         
        x      state vector  
        M      model structure  
        P      parameter vector  
         
        dfdx   Jacobian wrt states  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_phase_dfdx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_dfdx", *args, **kwargs)
