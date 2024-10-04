from spm.__wrap__ import _Runtime


def spm_mc_loss_G(*args, **kwargs):
  """  assumed potential gradient for the mountain car problem  
    problem  
    FORMAT [G] = spm_mc_loss_G(x,P)  
     
    x     - hidden states  
    v     - exogenous inputs  
    P.x,k - parameters for gradient function:     G(x(1),P.p)  
    P.q,q - parameters for cost or loss-function: C(x(1),P.q)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mc_loss_G.m)
  """

  return _Runtime.call("spm_mc_loss_G", *args, **kwargs)
