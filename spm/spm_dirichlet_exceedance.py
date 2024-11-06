from spm.__wrapper__ import Runtime


def spm_dirichlet_exceedance(*args, **kwargs):
    """
      Compute exceedance probabilities for a Dirichlet distribution  
        FORMAT xp = spm_dirichlet_exceedance(alpha,Nsamp)  
          
        Input:  
        alpha     - Dirichlet parameters  
        Nsamp     - number of samples used to compute xp [default = 1e6]  
          
        Output:  
        xp        - exceedance probability  
       __________________________________________________________________________  
         
        This function computes exceedance probabilities, i.e. for any given model  
        k1, the probability that it is more likely than any other model k2.    
        More formally, for k1=1..Nk and for all k2~=k1, it returns p(x_k1>x_k2)   
        given that p(x)=dirichlet(alpha).  
          
        Refs:  
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ  
        Bayesian Model Selection for Group Studies. NeuroImage (in press)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dirichlet_exceedance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dirichlet_exceedance", *args, **kwargs)
