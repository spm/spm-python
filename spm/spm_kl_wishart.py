from spm.__wrap__ import _Runtime


def spm_kl_wishart(*args, **kwargs):
  """  KL divergence between two Wishart densities  
    FORMAT [kl] = spm_kl_wishart(q,Q,p,P)  
     
    Calculate KL (Q||P) = <log Q/P> where avg is wrt Q  
    between two Wishart densities Q and P  
     
    q,Q      Parameters of first density  
    p,P      Parameters of first density  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_kl_wishart.m)
  """

  return _Runtime.call("spm_kl_wishart", *args, **kwargs)
