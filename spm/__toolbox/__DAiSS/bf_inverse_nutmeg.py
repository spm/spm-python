from spm.__wrapper__ import Runtime


def bf_inverse_nutmeg(*args, **kwargs):
  """  Interface to NUTMEG inverse methods   
    http://www.nitrc.org/plugins/mwiki/index.php/nutmeg:MainPage  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_nutmeg.m)
  """

  return Runtime.call("bf_inverse_nutmeg", *args, **kwargs)
