from spm.__wrapper__ import Runtime


def spm_beta_compare(*args, **kwargs):
    """
      Compute probability that r1 > r2  
        FORMAT xp = spm_beta_compare(alpha1,alpha2,Nsamp)  
          
        Input:  
        alpha1    - Beta parameters for first density  
        alpha2    - Beta parameters for second density  
        Nsamp     - number of samples used to compute xp [default = 1e4]  
          
        Output:  
        xp        - exceedance probability  
         
        Compute probability that r1 > r2 where p(r1)=Beta(r1|alpha1),   
        p(r2)=Beta(r2|alpha2). Uses sampling.   
        Useful for comparing groups in RFX model inference  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_beta_compare.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_beta_compare", *args, **kwargs)
