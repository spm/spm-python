from spm._runtime import Runtime


def spm_mdp_a2A(*args, **kwargs):
    r"""
      Dirichlet counts into probabilities   
        FORMAT MDP = spm_mdp_a2A(MDP,[FIX])  
        MDP{n} - Cell array of MDPs  
          
        FIX.A = 0 for learning likelihoods [default: 1]  
        FIX.B = 0 for learning transitions [default: 1]  
         
        This auxiliary routine converts Dirichlet likelihoods and (transition)  
        priors into expected probabilities. In other words, it replaces a with A  
        and b with B — for a hierarchical generative model.  
         
        see: spm_mdp2rdp.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mdp_a2A.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mdp_a2A", *args, **kwargs)
