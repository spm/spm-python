from spm._runtime import Runtime


def spm_MDP_VB_trial(*args, **kwargs):
    r"""
      auxiliary plotting routine for spm_MDP_VB - single trial  
        FORMAT spm_MDP_VB_trial(MDP,f,g)  
         
        MDP.P(M,T)      - probability of emitting action 1,...,M at time 1,...,T  
        MDP.X           - conditional expectations over hidden states  
        MDP.R           - conditional expectations over policies  
        MDP.o           - outcomes at time 1,...,T  
        MDP.s           - states at time 1,...,T  
        MDP.u           - action at time 1,...,T  
        f               - hidden states to show [default: 1:3]  
        g               - outcomes to show [default: 1:3]  
         
        MDP.un  = un;   - simulated neuronal encoding of hidden states  
        MDP.xn  = Xn;   - simulated neuronal encoding of policies  
        MDP.wn  = wn;   - simulated neuronal encoding of precision  
        MDP.da  = dn;   - simulated dopamine responses (deconvolved)  
         
        [f,g]           - factors and outcomes to plot [Default: first 3]  
         
        please see spm_MDP_VB. For multiple trials please see spm_MDP_VB_game  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_VB_trial.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_VB_trial", *args, **kwargs, nargout=0)
