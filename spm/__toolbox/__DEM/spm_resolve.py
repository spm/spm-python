from spm._runtime import Runtime


def spm_resolve(*args, **kwargs):
    r"""
      FORMAT mdp = spm_resolve(mdp)  
        mdp  - MDP structure  
         
        This subroutine concerns the reduction of a likelihood tensor by moving  
        posterior probability mass (Dirichlet counts) and assessing  the  
        resulting possterior beliefs (about parameters) in terms of expected free  
        energy which, in this instance, reduces to mutual information  
         
        This subroutine compresses transition tensors of Dirichlet parameters  
        summarising the joint distribution over outcomes and states. This  
        compression effectively minimises expected free energy by minimising  
        ambiguity; namely, the average conditional entropy over outcomes over  
        states. Because this minimisation entails moving posterior probability  
        mass between states, the entropy over outcomes remains the same and  
        therefore minimising ambiguity corresponds to maximising the mutual  
        information between states and outcomes. This can also be read as  
        minimising information loss.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_resolve.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_resolve", *args, **kwargs)
