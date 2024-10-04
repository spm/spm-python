from spm.__wrap__ import _Runtime


def bf_regularise_manual(*args, **kwargs):
  """  Manual specification of the regularisation parameter  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_manual.m)
  """

  return _Runtime.call("bf_regularise_manual", *args, **kwargs)
