from spm.__wrapper__ import Runtime


def spm_dcm_compare(*args, **kwargs):
  """  Compare two or more estimated models  
    FORMAT spm_dcm_compare(P)  
     
    P  - a char or cell array of DCM filenames  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_compare.m)
  """

  return Runtime.call("spm_dcm_compare", *args, **kwargs, nargout=0)
