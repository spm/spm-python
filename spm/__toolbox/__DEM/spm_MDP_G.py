from spm.__wrapper__ import Runtime


def spm_MDP_G(*args, **kwargs):
    """
      auxiliary function for Bayesian suprise or mutual information  
        FORMAT [G] = spm_MDP_G(A,x)  
         
        A   - likelihood array (probability of outcomes given causes)  
        x   - probability density of causes  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_G.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_G", *args, **kwargs)
