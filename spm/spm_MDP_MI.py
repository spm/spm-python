from spm._runtime import Runtime


def spm_MDP_MI(*args, **kwargs):
    r"""
      Expected information gain (i.e., mutual information)  
        FORMAT [E,dEda,dEdA] = spm_MDP_MI(a,c,h)  
         
        a    - Dirichlet parameters of a joint distribution  
        c    - prior preferences (outcomes)  
        h    - prior preferences (states)  
         
        E    - expected free energy (information gain minus cost)  
        dEda - derivative with respect to Dirichlet parameters (a)  
        dEdA - derivative with respect to joint density: A = a/sum(a(:))  
         
        The mutual information here pertains to the expected distribution. See  
        spm_dir_MI for the mutual information of a Dirichlet distribution per se  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MDP_MI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_MI", *args, **kwargs)
