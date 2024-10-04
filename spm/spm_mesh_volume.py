from spm.__wrap__ import _Runtime


def spm_mesh_volume(*args, **kwargs):
  """  Compute the volume of a closed surface mesh  
    FORMAT V = spm_mesh_volume(M)  
    M        - a patch structure  
      
    V        - volume  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_volume.m)
  """

  return _Runtime.call("spm_mesh_volume", *args, **kwargs)
