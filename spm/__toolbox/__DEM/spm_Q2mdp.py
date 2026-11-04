from spm._runtime import Runtime


def spm_Q2mdp(*args, **kwargs):
    r"""
      Dimensions (shape) of MDP based on generative model (a,b,...)   
        FORMAT [mdp] = spm_Q2mdp(Q,n)  
        s: states  
        u: paths  
        X: states (posterior)  
        Y: outcomes (predictive posterior)  
        O: outcomes (likelihood)  
        o: outcomes  
        j: outcomes (parents)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_Q2mdp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Q2mdp", *args, **kwargs)
