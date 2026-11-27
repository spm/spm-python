from spm._runtime import Runtime


def spm_RDP_prune(*args, **kwargs):
    r"""
      BMR of superordinate states based upon predicted outcomes  
        FORMAT [MDP,j] = spm_RDP_prune(MDP)  
        MDP  - cell array of MDP structures  
         
        MDP  - reduced MDP  
        j    - list of deep states with children  
         
        This routine prunes the leading factor of a renormalising generative  
        model by removing all childless states recursively, until all states are  
        transient (or there are no states).  
         
        see: https://en.wikipedia.org/wiki/Absorbing_Markov_chain  
       __________________________________________________________________________  
        Copyright (C) Karl Friston  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_prune.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_prune", *args, **kwargs)
