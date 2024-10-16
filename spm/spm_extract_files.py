from spm.__wrapper__ import Runtime


def spm_extract_files(*args, **kwargs):
  """  FORMAT spm_extract_files(P,cwd)  
    forints files (and their subroutines) and expect them to the current  
    directory  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_extract_files.m)
  """

  return Runtime.call("spm_extract_files", *args, **kwargs, nargout=0)
