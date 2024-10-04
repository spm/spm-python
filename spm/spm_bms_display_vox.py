from spm.__wrap__ import _Runtime


def spm_bms_display_vox(*args, **kwargs):
  """  Display results from BMS Maps at current voxel  
    FORMAT spm_bms_display_vox(BMS,xyz)  
     
    Input:  
    xyz - voxel coordinates [1,3] (voxel)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_display_vox.m)
  """

  return _Runtime.call("spm_bms_display_vox", *args, **kwargs, nargout=0)
