from spm._runtime import Runtime


def spm_mdp2rdp_a(*args, **kwargs):
    r"""
      Converts a cell array of MDPs into a recursive MDP (Dirichlet version)  
        FORMAT RDP = spm_mdp2rdp_a(MDP,p,q,T,FIX)  
        MDP{n} - Cell array of MDPs  
          
         MDP{n}.a    - likelihood tensors (Dirichlet)  
         MDP{n}.b    - transition tensors (Dirichlet)  
         MDP{n}.id.A - cell array of parents of A factors at the same level  
         MDP{n}.id.D - cell array of parents of D in supraordinate outcomes  
         MDP{n}.id.E - cell array of parents of E in supraordinate outcomes  
         
        p      - likelihood concentration; e.g., p = 1/32; [default: p = 0]   
        q      - prior (transition) decay; e.g., q = 1/32; [default: q = 0]   
        T      - path lengths [default: T = 2]  
          
        FIX.A = 0 for learning likelihoods  
        FIX.B = 0 for learning transitions  
         
        RDP    - likelihood and transition tensors for generating this sequence  
         RDP.L - level or depth  
         RDP.T - time steps  
         
        This auxiliary routine takes a cell array of hierarchically arranged  
        MDP’s and creates a single MDP where each subordinate MDP is a field of  
        the superordinate MDP. The vertical dependencies are encoded in the cell  
        arrays of parents at each level of the hierarchy, where the outcomes of  
        one level are the parents of the initial states and paths of the lower  
        level (encoded probabilistically in the vectors D and E of the lower  
        level).  
         
        In addition, this routine will remove redundant likelihood mappings, with  
        only one output. Factors with only one state are consolidated into a  
        single factor, which plays the role of a constant term; i.e., a unitary  
        state that always generates the same outcome.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mdp2rdp_a.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mdp2rdp_a", *args, **kwargs)
