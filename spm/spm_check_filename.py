from spm.__wrap__ import _Runtime


def spm_check_filename(*args, **kwargs):
  """  Check paths are valid and try to restore path names  
    FORMAT V = spm_check_filename(V)  
     
    V - struct array of file handles  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_check_filename.m)
  """

  return _Runtime.call("spm_check_filename", *args, **kwargs)
