from spm._runtime import Runtime


def spm_nwrnd(*args, **kwargs):
    r"""
      Generate N samples from Normal-Wishart density  
        FORMAT [m,Lambda,Cm] = spm_nwrnd (M,N)  
          
        Parameters M  
                  .a,.B,.beta,.m  
        N         number of samples  
         
        m         Means  
        Lambda    precisions  
        Cm        covariances  
         
        See J. Bernardo and A. Smith (2000)   
        Bayesian Theory, Wiley (page 435)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_nwrnd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_nwrnd", *args, **kwargs)
