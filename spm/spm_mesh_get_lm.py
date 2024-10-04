from spm.__wrap__ import _Runtime


def spm_mesh_get_lm(*args, **kwargs):
  """  Identification of local maxima on a textured surface mesh  
    FORMAT L = spm_mesh_get_lm(M,T)  
    M        - a [nx3] faces array or a patch structure or a [nxn] adjacency  
               matrix  
    T        - a [nx1] texture vector  
     
    L        - indices of vertices that are local maxima  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_get_lm.m)
  """

  return _Runtime.call("spm_mesh_get_lm", *args, **kwargs)
