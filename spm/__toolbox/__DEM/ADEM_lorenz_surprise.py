from spm.__wrapper__ import Runtime


def ADEM_lorenz_surprise(*args, **kwargs):
  """  This demo computes the cost-function (negative reward) for a Lorenz  
    system; to show cost can be computed easily from value (negative   
    surprise or sojourn time). However, value is not a Lyapunov function  
    because the flow is not curl-free (i.e., is not irrotational).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_lorenz_surprise.m)
  """

  return Runtime.call("ADEM_lorenz_surprise", *args, **kwargs, nargout=0)
