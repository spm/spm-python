from spm.__wrap__ import _Runtime


def _nut_dSPM(*args, **kwargs):
  """  [weight,eta]=nut_dSPM(Lp,data,flags)  
    Lp : lead field  
    inputs for regularization contant:  
    [1] data.Ryy = sample covariance, for data-dependent regularization  
    [2] flags.gamma = user defined regularization constant, or 'auto' for  
        leadfield-based regularization  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nut_dSPM.m)
  """

  return _Runtime.call("nut_dSPM", *args, **kwargs)
