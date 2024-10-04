from spm.__wrap__ import _Runtime


def spm_mesh_borders(*args, **kwargs):
  """  Return borders of a triangle mesh  
    FORMAT [B,C] = spm_mesh_borders(M)  
    M            - a [nx3] faces array or a patch handle/structure  
     
    B            - a [mx1] vector of indices of border vertices  
    C            - a cell array of indices of contiguous border vertices  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_borders.m)
  """

  return _Runtime.call("spm_mesh_borders", *args, **kwargs)
