from spm._runtime import Runtime


def spm_mci_init_flow(*args, **kwargs):
    r"""
      Extract init, flow and out params from rfx and ffx vectors  
        FORMAT [x_init,x_flow] = spm_mci_init_flow (assign,w,v,M)  
         
        assign    fields specify which are random/fixed effects  
        w         random effects vector  
        v         fixed effects vector  
        M         model structure  
         
        x_init    init params  
        x_flow    flow params (includes out params)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_init_flow.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_init_flow", *args, **kwargs)
