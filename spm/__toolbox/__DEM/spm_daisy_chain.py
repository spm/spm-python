from spm._runtime import Runtime


def spm_daisy_chain(*args, **kwargs):
    r"""
      Selctive structure learning of a hierarchical POMDP  
        FORMAT MDP = spm_daisy_chain(R,S,MDP,GDP)  
        R    - cell array of outcomes  
        S    - cell array (attracting set) of output sequences  
        MDP  - cell array of (renormalising) models  
         
        MDP  - new MDP  
        O    - cell array of new paths in MDP  
         
        This routine uses fast structure learning to append new trajectories to a  
        recursive or renormalising generative model specified as a cell array of  
        Markov decision processes. It augments past (generalised) states and  
        transitions with new states and transitions given new outcomes (R), under  
        the constraint that each event ends on the attracting set (S)  
         
        See: spm_fast_structure_learning.m  
             spm_faster_structure_learning.m  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_daisy_chain.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_daisy_chain", *args, **kwargs)
