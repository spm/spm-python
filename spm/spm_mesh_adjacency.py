from spm.__wrap__ import _Runtime


def spm_mesh_adjacency(*args, **kwargs):
  """  Compute the adjacency matrix of a triangle mesh  
    FORMAT A = spm_mesh_adjacency(F)  
    F        - a [fx3] faces array or a patch structure  
      
    A        - adjacency matrix as a sparse [vxv] array  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_adjacency.m)
  """

  return _Runtime.call("spm_mesh_adjacency", *args, **kwargs)
