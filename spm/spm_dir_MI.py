from spm._runtime import Runtime


def spm_dir_MI(*args, **kwargs):
    r"""
      Expected information gain (i.e., mutual information)  
        FORMAT [E] = spm_dir_MI(a,c,h)  
         
        a    - Dirichlet parameters of a joint distribution  
        c    - prior preferences (outcomes)  
        h    - prior preferences (states)  
         
        E    - expected free energy (information gain minus cost)  
         
        The mutual information here pertains to the Dirichlet distribution. See  
        spm_MDP_MI for the mutual information of the expected categorical  
        distribution.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dir_MI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_MI", *args, **kwargs)
