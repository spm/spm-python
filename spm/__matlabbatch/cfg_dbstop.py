from spm.__wrapper__ import Runtime


def cfg_dbstop(*args, **kwargs):
  """cfg_dbstop is a function.  
      cfg_dbstop(fh)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_dbstop.m)
  """

  return Runtime.call("cfg_dbstop", *args, **kwargs, nargout=0)
