from spm._runtime import Runtime


def spm_check_edges(*args, **kwargs):
    r"""
      Converts a recursive MDP into a cell array of MDPs   
        FORMAT MDP = spm_check_edges(RDP)  
         
        RDP    - Deep (recursive) MDP (i.e., RDP.MDP.MDP...)    
         RDP.L - level or depth  
         RDP.T - time steps  
         
        MDP{n} - Cell array of MDPs  
         MDP{n}.A    - likelihood tensors   
         MDP{n}.B    - transition tensors (logical)  
         MDP{n}.id.A - cell array of parents of A factors at the same level  
         MDP{n}.id.B - cell array of parents of B factors at the same level  
         MDP{n}.id.C - cell array of parents of C priors  at the same level  
         MDP{n}.id.D - cell array of parents of initial state at next level  
         MDP{n}.id.E - cell array of parents of initial paths at next level  
         
        This auxiliary routine takes a single MDP where each subordinate MDP is a  
        field of the superordinate MDP and creates a cell array of hierarchically  
        arranged MDP’s. The vertical dependencies are encoded in the cell arrays  
        of parents at each level of the hierarchy, where the outcomes of one  
        level are the parents of the initial states and paths of the lower level  
        (encoded probabilistically in the vectors D and E of the lower level).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_check_edges.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_check_edges", *args, **kwargs)
