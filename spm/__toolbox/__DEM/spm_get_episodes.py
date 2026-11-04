from spm._runtime import Runtime


def spm_get_episodes(*args, **kwargs):
    r"""
      Gets rewarded (and restricted) states at the deepest level of an MDP  
        FORMAT [HID,CID,HITS,MISS] = spm_get_episodes(hid,cid,GDP,MDP)  
        hid  - List of intended (i.e., rewarded) goal states at the lowest level  
        cid  - List of constrained (i.e., restricted) states at the lowest level  
        GDP  - Generative process  
        MDP  - Generative models (hierarchical)  
         
        HID  - List of intended (i.e., rewarded) goal states at highest level  
        CID  - List of constrained (i.e., restricted) states at highest level  
        HITS - List of intended (i.e. rewarded) goal outcomes at lowest level  
        MISS - List of constrained (i.e. restricted) outcomes at lowest level  
         
       --------------------------------------------------------------------------  
        This auxiliary routine identifies the episodes (i.e., paths) encoded by  
        states at the deepest or highest level of a hierarchical MDP that entail  
        one or more intended states at the lowest level.  
         
        For convenience, it assumes the intended outcomes in HITS correspond to  
        the first set of outcomes generated from each highest (generalised)  
        latent state.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_get_episodes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_episodes", *args, **kwargs)
