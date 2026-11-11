from spm._runtime import Runtime


def spm_MDP_G(*args, **kwargs):
    r"""
      auxiliary function for Bayesian suprise or mutual information  
        FORMAT [G] = spm_MDP_G(A,x)  
         
        A   - likelihood array (probability of outcomes given causes)  
        x   - probability density of causes  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_G.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_G", *args, **kwargs)
