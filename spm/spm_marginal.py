from spm.__wrapper__ import Runtime


def spm_marginal(*args, **kwargs):
  """  Marginal densities over a multidimensional array of probabilities  
    FORMAT [Y] = spm_marginal(X)  
    X  - numeric array of probabilities  
     
    Y  - cell array of marginals  
     
    See also: spm_dot  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_marginal.m)
  """

  return Runtime.call("spm_marginal", *args, **kwargs)
