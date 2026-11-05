from spm._runtime import Runtime


def spm_set_goals(*args, **kwargs):
    r"""
      Gets rewarded (and restricted) states at the deepest level of an MDP  
        FORMAT MDP = spm_set_goals(MDP,S,chi)  
        MDP  - Generative model (hierarchical)  
        S    - list of modality streams;    e.g., [ 2,3]  
        chi  - log prior for each modality; e.g., [-8,8]    
         
       --------------------------------------------------------------------------  
        This auxiliary routine identifies the episodes (i.e., paths) encoded by  
        states at the deepest or highest level of a hierarchical MDP that entail  
        intended or avoided outcomes at the lowest level.These intended or costly  
        latent states are indexed in MDP{end}.id.hid and MDP{end}.id.cid,  
        respectively — in the highest level identifier field.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_set_goals.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_set_goals", *args, **kwargs)
