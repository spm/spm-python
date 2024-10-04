from spm.__wrap__ import _Runtime


def spm_kl_dirichlet(*args, **kwargs):
  """  KL divergence between two Dirichlet densities  
    FORMAT [d] = spm_kl_dirichlet(lambda_q,lambda_p,log_tilde_pi)  
     
    Calculate KL (Q||P) = <log Q/P> where avg is wrt Q  
    between two Dirichlet densities Q and P  
     
    lambda_q      Parameter vector of first density  
    lambda_p      Parameter vector of second density  
    log_tilde_pi  <log (pi)> where avg is over Q. If this argument  
                  isn't passed the routine will calculate it  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_kl_dirichlet.m)
  """

  return _Runtime.call("spm_kl_dirichlet", *args, **kwargs)
