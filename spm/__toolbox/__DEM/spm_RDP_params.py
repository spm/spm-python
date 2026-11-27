from spm._runtime import Runtime


def spm_RDP_params(*args, **kwargs):
    r"""
      Show prior transition parameters for a recursive or renormalising model  
        FORMAT spm_RDP_params(MDP)  
        MDP - MDP structure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_params.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_params", *args, **kwargs, nargout=0)
