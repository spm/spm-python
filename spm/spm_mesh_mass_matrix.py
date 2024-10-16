from spm.__wrapper__ import Runtime


def spm_mesh_mass_matrix(*args, **kwargs):
  """  Compute the mass matrix of a triangle mesh  
    M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
     
    A        - Mass matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_mass_matrix.m)
  """

  return Runtime.call("spm_mesh_mass_matrix", *args, **kwargs)
