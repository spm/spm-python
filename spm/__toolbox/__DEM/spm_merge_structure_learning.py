from spm._runtime import Runtime


def spm_merge_structure_learning(*args, **kwargs):
    r"""
      RG structure learning of a hierarchical POMDP  
        FORMAT MDP = spm_merge_structure_learning(O,MDP)  
        O{N,T} - cell array of (probabilisitc) outcomes  
        MDP    - cell array of (renormalising) models  
         
        This routine uses fast structure learning to append or merge new  
        trajectories to a recursive or renormalising generative model specified  
        as a cell array of Markov decision processes. It augments past  
        (generalised) states and transitions with new states and transitions  
        under the assumption that the first states have been seen before.  
         
        See: spm_fast_structure_learning.m  
             spm_faster_structure_teaching.m  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_merge_structure_learning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_merge_structure_learning", *args, **kwargs)
