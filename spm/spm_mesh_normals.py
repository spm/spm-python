from spm.__wrap__ import _Runtime


def spm_mesh_normals(*args, **kwargs):
  """  Compute (unit) normals of a surface mesh  
    FORMAT [Nv, Nf] = spm_mesh_normals(M, unit)  
    M      - a patch structure or a handle to a patch  
    unit   - boolean to indicate unit normals or not [default: false]  
     
    Nv     - a [nx3] array of (unit) normals on vertices  
    Nf     - a [mx3] array of (unit) normals on faces  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_normals.m)
  """

  return _Runtime.call("spm_mesh_normals", *args, **kwargs)
