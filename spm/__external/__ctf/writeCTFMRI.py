from spm.__wrapper__ import Runtime


def writeCTFMRI(*args, **kwargs):
  """  Version 1.2   25 April 2007   Module writeCPersist changed, and removed from this text  
                                  file.  
    Version 1.1   19 April 2007 : No changes from v1.0  
    Version 1.0   27 Oct. 2006  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/writeCTFMRI.m)
  """

  return Runtime.call("writeCTFMRI", *args, **kwargs, nargout=0)
