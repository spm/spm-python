from spm._runtime import Runtime


def spm_MDP_params(*args, **kwargs):
    r"""
      Show likelihood and prior transition parameters  
        FORMAT spm_MDP_params(MDP,OPT)  
         
        MDP - MDP structure  
        OPT - normalise [1]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_params.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_params", *args, **kwargs, nargout=0)
