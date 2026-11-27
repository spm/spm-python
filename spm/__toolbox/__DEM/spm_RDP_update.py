from spm._runtime import Runtime


def spm_RDP_update(*args, **kwargs):
    r"""
      places parameters in a recursive model  
        FORMAT RDP = spm_RDP_update(MDP,PDP,[BMR])  
        MDP - nested MDP: prior  
        PDP - nested MDP: posterior (with PDP.Q)  
        BMR - Bayesian model reduction {'SIMPLE','MI'} [default: none]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_update.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_update", *args, **kwargs)
