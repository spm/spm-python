from spm.__wrapper__ import Runtime


def spm_MDP_VB_game(*args, **kwargs):
    """
      auxiliary plotting routine for spm_MDP_VB - multiple trials  
        FORMAT Q = spm_MDP_VB_game(MDP)  
         
        MDP.P(M,T)      - probability of emitting action 1,...,M at time 1,...,T  
        MDP.X           - conditional expectations over hidden states  
        MDP.R           - conditional expectations over policies  
        MDP.O(O,T)      - a sparse matrix encoding outcomes at time 1,...,T  
        MDP.S(N,T)      - a sparse matrix encoding states at time 1,...,T  
        MDP.U(M,T)      - a sparse matrix encoding action at time 1,...,T  
        MDP.W(1,T)      - posterior expectations of precision  
         
        MDP.xn  = Xn    - simulated neuronal encoding of policies  
        MDP.wn  = wn    - simulated neuronal encoding of precision  
        MDP.da  = dn    - simulated dopamine responses (deconvolved)  
        MDP.rt  = rt    - simulated dopamine responses (deconvolved)  
         
        returns summary of performance:  
         
            Q.X  = x    - expected hidden states  
            Q.R  = u    - final policy expectations  
            Q.S  = s    - initial hidden states  
            Q.O  = o    - final outcomes  
            Q.p  = p    - performance  
            Q.q  = q    - reaction times  
         
        please see spm_MDP_VB  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB_game.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB_game", *args, **kwargs)
