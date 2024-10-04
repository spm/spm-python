from spm.__wrap__ import _Runtime


def spm_reorder_contrasts(*args, **kwargs):
  """  Recompute contrasts allowing for permutation and deletion  
    FORMAT batch = spm_reorder_contrasts(SPM,order)  
    SPM   - SPM data structure  
    order - array of contrast indices  
     
    batch - batch job  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_reorder_contrasts.m)
  """

  return _Runtime.call("spm_reorder_contrasts", *args, **kwargs)
