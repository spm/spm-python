from spm.__wrap__ import _Runtime


def ADEM_plaid(*args, **kwargs):
  """  creates a Gaussian modulated n x n visual plaid stimulus  
    FORMAT [y,n] = ADEM_plaid(x,[n])  
    x(1) - horizontal displacement  
    x(2) - vertical displacement  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_plaid.m)
  """

  return _Runtime.call("ADEM_plaid", *args, **kwargs)
