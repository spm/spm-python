from spm.__wrapper__ import Runtime


def _nut_swLORETA(*args, **kwargs):
  """  [weight,eta]=nut_swLORETA(Lp,data,flags)  
    Lp : lead field ( channels X 3 )  
    specify either:  
    [1] data.Ryy (sample covariance) normally required (used for data-dependent regularization)  
            currently sets gamma = max(eig(data.Ryy))  
            [probably should be set lower for best compromise between stability and blurriness]  
    [2] flags.gamma = regularization constant [optional]  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nut_swLORETA.m)
  """

  return Runtime.call("nut_swLORETA", *args, **kwargs)
