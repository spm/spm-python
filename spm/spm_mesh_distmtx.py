from spm.__wrap__ import _Runtime


def spm_mesh_distmtx(*args, **kwargs):
  """  Compute the distance matrix of a triangle mesh  
    FORMAT D = spm_mesh_distmtx(M,order)  
    M        - patch structure  
    order    - 0: adjacency matrix  
               1: first order distance matrix [default]  
               2: second order distance matrix  
     
    D        - distance matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_distmtx.m)
  """

  return _Runtime.call("spm_mesh_distmtx", *args, **kwargs)
