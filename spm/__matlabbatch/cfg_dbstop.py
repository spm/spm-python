from spm.__wrap__ import _Runtime


def cfg_dbstop(*args, **kwargs):
  """cfg_dbstop is a function.  
      cfg_dbstop(fh)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_dbstop.m)
  """

  return _Runtime.call("cfg_dbstop", *args, **kwargs, nargout=0)
