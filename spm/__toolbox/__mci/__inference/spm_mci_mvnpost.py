from spm.__wrapper__ import Runtime


def spm_mci_mvnpost(*args, **kwargs):
  """  Are MCMC samples consistent with Gaussian posterior ?  
    FORMAT [stats,Y,X] = spm_mci_mvnpost (post,method,verbose,max_lag)  
     
    post      posterior data structure from spm_mci_post  
    method    'ESS' or 'thinning'  
    verbose   create plots  
    max_lag   maximum potential lag for MAR model  
      
    stats     (multivariate) normal test statistics  
              See spm_mci_mvntest.m  
    Y         uncorrelated posterior samples  
    X         original posterior samples  
      
    Run Gaussianity test on Markov chain samples  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mvnpost.m)
  """

  return Runtime.call("spm_mci_mvnpost", *args, **kwargs)
