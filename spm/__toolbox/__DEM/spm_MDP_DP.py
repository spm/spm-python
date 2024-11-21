from spm.__wrapper__ import Runtime


def spm_MDP_DP(*args, **kwargs):
    """
      dynamic programming using active inference  
        FORMAT [B0,BV] = spm_MDP_DP(MDP)  
         
        MDP.A(O,N)      - Likelihood of O outcomes given N hidden states  
        MDP.B{M}(N,N)   - transition probabilities among hidden states (priors)  
        MDP.C(N,1)      - prior preferences (prior over future states)  
         
        MDP.V(T - 1,P)  - P allowable policies (control sequences)  
         
        B0      - optimal state action policy or transition matrix  
        BV      - corresponding policy using value iteration  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_DP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_DP", *args, **kwargs)
