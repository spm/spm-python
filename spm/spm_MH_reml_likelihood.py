from spm.__wrapper__ import Runtime


def spm_MH_reml_likelihood(*args, **kwargs):
  """  Likelihood function for spm_MH_reml  
    FORMAT [L] = spm_MH_reml_likelihood(h,Y,M)  
     
    h - hyperparameters  
    Y - residual covariance  
     
    L - likelihood p(Y,P)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_MH_reml_likelihood.m)
  """

  return Runtime.call("spm_MH_reml_likelihood", *args, **kwargs)
