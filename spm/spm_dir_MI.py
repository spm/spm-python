from spm.__wrapper__ import Runtime


def spm_dir_MI(*args, **kwargs):
    """
      Expected information gain (i.e., mutual information)  
        FORMAT E = spm_dir_MI(a)  
         
        a    - Dirichlet parameters of a joint distribution  
        C    - log preferences  
         
        E    - expected free energy (information gain minus cost)  
         
        The mutual information here pertains to the Dirichlet distribution. See  
        spm_MDP_MI for the mutual information of the expected categorical  
        distribution.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dir_MI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dir_MI", *args, **kwargs)
