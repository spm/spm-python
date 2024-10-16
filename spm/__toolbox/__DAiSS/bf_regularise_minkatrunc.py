from spm.__wrapper__ import Runtime


def bf_regularise_minkatrunc(*args, **kwargs):
  """  Bayesian regularisation based on Minka's method  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_minkatrunc.m)
  """

  return Runtime.call("bf_regularise_minkatrunc", *args, **kwargs)
