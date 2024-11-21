from spm.__wrapper__ import Runtime


def spm_MDP_MI(*args, **kwargs):
    """
      Expected information gain (i.e., mutual information)  
        FORMAT [E,dEda,dEdA] = spm_MDP_MI(a,C)  
         
        a    - Dirichlet parameters of a joint distribution  
        C    - log preferences  
         
        E    - expected free energy (information gain minus cost)  
        dEda - derivative with respect to Dirichlet parameters (a)  
        dEdA - derivative with respect to joint density: A = a/sum(a(:))  
         
        The mutual information here pertains to the expected distribution. See  
        spm_dir_MI for the mutual information of a Dirichlet distribution per se  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_MDP_MI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_MI", *args, **kwargs)
