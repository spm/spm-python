from spm._runtime import Runtime


def spm_mci_flow_t(*args, **kwargs):
    r"""
      Evaluate flow at time t  
        FORMAT [dxdt] = spm_mci_flow_t (t,x,U,P,M)  
         
        t     time  
        x     state  
        U     inputs  
        P     parameters  
        M     model  
         
        dxdt  flow, dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/gradients/spm_mci_flow_t.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_flow_t", *args, **kwargs)
