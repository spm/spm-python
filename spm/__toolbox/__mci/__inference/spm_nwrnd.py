from spm.__wrapper__ import Runtime


def spm_nwrnd(*args, **kwargs):
  """  Generate N samples from Normal-Wishart density  
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
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_nwrnd.m)
  """

  return Runtime.call("spm_nwrnd", *args, **kwargs)
