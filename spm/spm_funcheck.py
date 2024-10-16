from spm.__wrapper__ import Runtime


def spm_funcheck(*args, **kwargs):
  """  Convert strings and inline objects to function handles  
    FORMAT [h] = spm_funcheck(f)  
     
    f   - filename, character expression or inline function  
    h   - corresponding function handle  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_funcheck.m)
  """

  return Runtime.call("spm_funcheck", *args, **kwargs)
