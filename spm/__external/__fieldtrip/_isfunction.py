from spm.__wrapper__ import Runtime


def _isfunction(*args, **kwargs):
  """  ISFUNCTION tests whether the function of the specified name is a callable  
    function on the current MATLAB path.  
     
    Note that this is *not* equivalent to calling exist(funcname, 'file'),  
    since that will return 7 in case funcname exists as a folder.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/isfunction.m)
  """

  return Runtime.call("isfunction", *args, **kwargs)
