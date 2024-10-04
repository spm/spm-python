from spm.__wrap__ import _Runtime


def spm_unlink(*args, **kwargs):
  """  Silently delete files on disk - a compiled routine  
    FORMAT spm_unlink('file1','file2','file3','file4',...)  
     
    Remove the specified file(s) using a system call to unlink().  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_unlink.m)
  """

  return _Runtime.call("spm_unlink", *args, **kwargs, nargout=0)
