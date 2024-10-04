from spm.__wrap__ import _Runtime


def spm_dcm_compare(*args, **kwargs):
  """  Compare two or more estimated models  
    FORMAT spm_dcm_compare(P)  
     
    P  - a char or cell array of DCM filenames  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_compare.m)
  """

  return _Runtime.call("spm_dcm_compare", *args, **kwargs, nargout=0)
