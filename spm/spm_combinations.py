from spm.__wrap__ import _Runtime


def spm_combinations(*args, **kwargs):
  """  FORMAT U = spm_combinations(Nu)  
    Nu  - vector of dimensions  
    U   - combinations of indices  
     
    returns a matrix of all combinations of Nu  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_combinations.m)
  """

  return _Runtime.call("spm_combinations", *args, **kwargs)
