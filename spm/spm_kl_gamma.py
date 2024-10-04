from spm.__wrap__ import _Runtime


def spm_kl_gamma(*args, **kwargs):
  """  KL divergence between two Gamma densities  
    FORMAT [d] = spm_kl_gamma(b_q,c_q,b_p,c_p)  
     
    KL (Q||P) = <log Q/P> where avg is wrt Q  
     
    b_q, c_q    Parameters of first Gamma density  
    b_p, c_p    Parameters of second Gamma density  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_kl_gamma.m)
  """

  return _Runtime.call("spm_kl_gamma", *args, **kwargs)
