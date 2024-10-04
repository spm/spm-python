from spm.__wrap__ import _Runtime


def spm_KL_dir(*args, **kwargs):
  """  KL divergence between two Dirichlet distributions  
    FORMAT [d] = spm_kl_dir(lambda_q,lambda_p)  
     
    Calculate KL(Q||P) = <log Q/P> where avg is wrt Q between two Dirichlet   
    distributions Q and P  
     
    lambda_q   -   concentration parameter matrix of Q  
    lambda_p   -   concentration parameter matrix of P  
     
    This routine uses an efficient computation that handles arrays, matrices   
    or vectors. It returns the sum of divergences over columns.  
     
    See also: spm_kl_dirichlet.m (for row vectors)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_KL_dir.m)
  """

  return _Runtime.call("spm_KL_dir", *args, **kwargs)
