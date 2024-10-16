from spm.__wrapper__ import Runtime


def covLin(*args, **kwargs):
  """  Covariance function for linear regression/classification  
    FORMAT [K1,lambda] = covLin(lambda0,settings,args,lab)  
    No usage documentation yet  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/covLin.m)
  """

  return Runtime.call("covLin", *args, **kwargs)
