from spm.__wrap__ import _Runtime


def spm_authors(*args, **kwargs):
  """  Return list of SPM coauthors  
    FORMAT [current, previous] = spm_authors  
    current  - cell array of SPM coauthors of the current release  
    previous - cell array of SPM coauthors of previous releases  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_authors.m)
  """

  return _Runtime.call("spm_authors", *args, **kwargs)
