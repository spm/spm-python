from spm._runtime import Runtime


def spm_MDP_link(*args, **kwargs):
    r"""
      auxiliary function to create link (cell array)  
        FORMAT [LINK,link] = spm_MDP_link(MDP)  
         
        MDP.MDP  - hierarchical MDP structure  
         
        LINK  - cell array of (binary) matrices linking outputs to states  
        link  - (binary) matrix of non-empty links  
         
        this routine assumes unique names in MDP.labels  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_link.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_link", *args, **kwargs)
