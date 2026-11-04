from spm._runtime import Runtime


def spm_faster_structure_learning(*args, **kwargs):
    r"""
      RG structure learning of a hierarchical POMDP  
        FORMAT [MDP] = spm_faster_structure_learning(O,S,dx,dt)  
        O{N,T} - probabilitic exemplars of paths (cell aray)  
        S      - array size of streams (number of streams x 4)  
           S(:,1) - size (x) of group in each stream    
           S(:,2) - size (y) of group in each stream   
           S(:,3) - size (z) of group in each stream   
           S(:,4) - number of outcomes per group in each stream   
        dx     - space scaling [default: 2]  
        dt     - time  scaling [default: 2]  
         
        This routine returns a hierarchy of generative models (MDP{n}), given a  
        sequence of outcomes using RG (renormalization group) operators. Output  
        modalities are segregated into distinct streams (as specified by the size  
        of groups:  S). The likelihood mappings within each stream maximise  
        mutual information between successive levels by retaining unique  
        combinations of outcomes over groups within each stream. These unique  
        combinations are identified using the information distance between  
        outcomes at each level. Between stream likelihoods map from the first or  
        principal stream to subsequent or trailing streams, which will usually be  
        the consequences of generalised states generated in the principal stream.  
         
        See also: spm_MDP_structure_learning.m  
                  spm_MDP_structure_teaching.m  
                  spm_merge_structure_learning  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_faster_structure_learning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_faster_structure_learning", *args, **kwargs)
