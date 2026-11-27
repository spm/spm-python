from spm._runtime import Runtime


def spm_fast_structure_learning(*args, **kwargs):
    r"""
      RG structure learning of a hierarchical POMDP  
        FORMAT [MDP,RG,S] = spm_fast_structure_learning(O,S)  
        O{N,T} - probabilitic exemplars of paths (cell aray)  
        S      - size of pixel array (2 or 3-vector)  
         
        dx     - space scaling [default: 2 or 3]  
        dt     - time  scaling [default: 2]  
         
        This routine returns a hierarchy of generative models (MDP{n}), given a  
        sequence of outcomes using RG (renormalization group) operators.  
         
        See: spm_MDP_structure_learning.m  
             spm_MDP_structure_teaching.m  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fast_structure_learning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fast_structure_learning", *args, **kwargs)
