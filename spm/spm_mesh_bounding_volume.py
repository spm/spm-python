from spm.__wrap__ import _Runtime


def spm_mesh_bounding_volume(*args, **kwargs):
  """  Bounding volume of a triangle mesh  
    FORMAT bv = spm_mesh_bounding_volume(M,t)  
    M        - a patch structure or GIfTI object  
    t        - type of bounding volume [default: 'AABB']  
     
    bv       - bounding volume  
   __________________________________________________________________________  
     
    See: https://en.wikipedia.org/wiki/Bounding_volume  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_bounding_volume.m)
  """

  return _Runtime.call("spm_mesh_bounding_volume", *args, **kwargs)
