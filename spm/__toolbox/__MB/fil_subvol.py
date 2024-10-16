from spm.__wrapper__ import Runtime


def fil_subvol(*args, **kwargs):
  """  Dimensions and voxel-to world mapping of a subvolume  
    FORMAT [d,M] = fil_subvol(Nii,bb)  
    Nii    - SPM NIfTI object  
    bb     - bounding box (2 x 3)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/fil_subvol.m)
  """

  return Runtime.call("fil_subvol", *args, **kwargs)
