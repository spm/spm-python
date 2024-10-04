from spm.__wrap__ import _Runtime


def spm_mesh_inflate(*args, **kwargs):
  """  Surface mesh inflation  
    FORMAT M = spm_mesh_inflate(M,T,S)  
     
    M        - surface mesh structure (see patch) or GIfTI object  
               or handle to a patch in a figure  
    T        - number of time steps [default: Inf (auto)]  
    S        - update display every S time steps [default: 0 (never)]  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_inflate.m)
  """

  return _Runtime.call("spm_mesh_inflate", *args, **kwargs)
