from spm.__wrapper__ import Runtime


def _nut_sLORETA(*args, **kwargs):
  """  weight=nut_sLORETA(Lp,data,flags)  
    inputs for regularization contant:  
    [1] data.Ryy = sample covariance, for data-dependent regularization  
    [2] flags.gamma = user defined regularization constant, or 'auto' for  
        leadfield-based regularization  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nut_sLORETA.m)
  """

  return Runtime.call("nut_sLORETA", *args, **kwargs)
