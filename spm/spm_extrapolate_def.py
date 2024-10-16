from spm.__wrapper__ import Runtime


def spm_extrapolate_def(*args, **kwargs):
  """  Fill in non-finite values in a deformation field  
    FORMAT Y = spm_extrapolate_def(Y,M)  
    Y - the deformation field  
    M - voxel-to-world transform associated with the deformation  
        (for deriving voxel sizes)  
     
    This function is typically used after generating an inverse deformation,  
    as these may contain missing locations.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_extrapolate_def.m)
  """

  return Runtime.call("spm_extrapolate_def", *args, **kwargs)
