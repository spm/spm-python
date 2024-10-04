from spm.__wrap__ import _Runtime


def mci_linear_post(*args, **kwargs):
  """  Analytic posterior for linear regression  
    FORMAT [Ep,Cp,L] = mci_linear_post (M,U,Y)  
      
    M     Model Structure  
    U     Inputs  
    Y     Data  
     
    Ep    Posterior mean  
    Cp    Posterior covariance  
    L     Log evidence  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_post.m)
  """

  return _Runtime.call("mci_linear_post", *args, **kwargs)
