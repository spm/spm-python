from spm._runtime import Runtime


def spm_MB_structure_learning(*args, **kwargs):
    r"""
      RG structure learning of a hierarchical POMDP  
        FORMAT [MDP,LG,RG] = spm_MB_structure_learning(O,L,dt)  
        O{N,T} - probabilitic exemplars of paths (cell aray)  
        L      - array of pixel locations  
        dt     - time dilation [1 for images]  
         
        MDP{n} - cell aray of MDPs  
        RG{n}  - cell aray of group indices  
        LG{n}  - cell aray of locations  
         
        This routine returns a hierarchy of generative models (MDP{n}), given a  
        sequence of outcomes using RG (renormalization group) operators.  
         
        see: spm_MDP_structure_learning.m  
             spm_MDP_structure_teaching.m  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MB_structure_learning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MB_structure_learning", *args, **kwargs)
