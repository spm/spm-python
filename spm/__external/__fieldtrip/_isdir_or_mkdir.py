from spm.__wrapper__ import Runtime


def _isdir_or_mkdir(*args, **kwargs):
  """  ISDIR_OR_MKDIR Checks that a directory exists, or if not, creates the directory and  
    all its parent directories.  
     
    See also FOPEN_OR_ERROR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/isdir_or_mkdir.m)
  """

  return Runtime.call("isdir_or_mkdir", *args, **kwargs, nargout=0)
