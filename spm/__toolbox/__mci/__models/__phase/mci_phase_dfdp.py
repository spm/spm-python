from spm._runtime import Runtime


def mci_phase_dfdp(*args, **kwargs):
    r"""
      Parameter sensitivity for phase model  
        FORMAT [dfdp] = mci_phase_dfdp (x,u,P,M)  
         
        x      State vector  
        u      inputs  
        P      parameter vector  
        M      model structure  
         
        dfdp   Jacobian wrt. parameters, df/dp  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_phase_dfdp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_dfdp", *args, **kwargs)
