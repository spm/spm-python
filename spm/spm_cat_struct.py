from spm.__wrapper__ import Runtime


def spm_cat_struct(*args, **kwargs):
  """  Concatenates structure arrays with possibly different fields  
    FORMAT s = spm_cat_struct(s1, s2, ...)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cat_struct.m)
  """

  return Runtime.call("spm_cat_struct", *args, **kwargs)
