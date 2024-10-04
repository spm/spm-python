from spm.__wrap__ import _Runtime


def bf_regularise_tichonov_rankdef(*args, **kwargs):
  """  Tichonov regularisation for rank deficient matrices based on the function  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_tichonov_rankdef.m)
  """

  return _Runtime.call("bf_regularise_tichonov_rankdef", *args, **kwargs)
