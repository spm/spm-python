from spm.__wrap__ import _Runtime


def spm_mesh_mass_matrix(*args, **kwargs):
  """  Compute the mass matrix of a triangle mesh  
    M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
     
    A        - Mass matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_mass_matrix.m)
  """

  return _Runtime.call("spm_mesh_mass_matrix", *args, **kwargs)
