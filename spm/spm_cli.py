from spm.__wrapper__ import Runtime


def spm_cli(*args, **kwargs):
  """  Command line interface for SPM  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cli.m)
  """

  return Runtime.call("spm_cli", *args, **kwargs, nargout=0)
