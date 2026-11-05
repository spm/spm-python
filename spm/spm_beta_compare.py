from spm._runtime import Runtime


def spm_beta_compare(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_beta_compare.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_beta_compare", *args, **kwargs)
