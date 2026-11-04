from spm._runtime import Runtime


def spm_MDP_size(*args, **kwargs):
    r"""
      Dimensions (shape) of MDP based on generative model (a,b,...)   
        FORMAT [Nf,Ns,Nu,Ng,No] = spm_MDP_size(mdp)  
        Nf  - number of factors  
        Ns  - states per factor  
        Nu  - control per factors  
        Ng  - number of modalities  
        No  - levels per modality  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_size.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_size", *args, **kwargs)
