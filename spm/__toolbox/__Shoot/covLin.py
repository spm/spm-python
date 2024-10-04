from spm.__wrap__ import _Runtime


def covLin(*args, **kwargs):
  """  Covariance function for linear regression/classification  
    FORMAT [K1,lambda] = covLin(lambda0,settings,args,lab)  
    No usage documentation yet  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/covLin.m)
  """

  return _Runtime.call("covLin", *args, **kwargs)
