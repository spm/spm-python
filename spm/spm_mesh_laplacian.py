from spm.__wrap__ import _Runtime


def spm_mesh_laplacian(*args, **kwargs):
  """  Compute the graph or (cotangent) mesh Laplacian  
    M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
    T        - {'graph','mesh'} [Default: 'graph']  
     
    L        - Laplacian  
   __________________________________________________________________________  
     
    Laplacian matrix:  
      https://en.wikipedia.org/wiki/Laplacian_matrix  
      https://en.wikipedia.org/wiki/Discrete_Laplace_operator#Mesh_Laplacians  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_laplacian.m)
  """

  return _Runtime.call("spm_mesh_laplacian", *args, **kwargs)
