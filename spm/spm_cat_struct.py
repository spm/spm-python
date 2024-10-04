from spm.__wrap__ import _Runtime


def spm_cat_struct(*args, **kwargs):
  """  Concatenates structure arrays with possibly different fields  
    FORMAT s = spm_cat_struct(s1, s2, ...)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cat_struct.m)
  """

  return _Runtime.call("spm_cat_struct", *args, **kwargs)
