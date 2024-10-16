from spm.__wrapper__ import Runtime


def spm_mesh_to_grid(*args, **kwargs):
  """  Non-linear interpolation of surface-based data onto a regular grid  
    FORMAT R = spm_mesh_to_grid(M, V, T)  
    M        - a patch structure with fields 'faces' and 'vertices'  
    V        - an spm_vol structure with fields 'dim' and 'mat'  
    T        - array of data to be interpolated  
     
    R        - interpolated data on grid defined by V  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_to_grid.m)
  """

  return Runtime.call("spm_mesh_to_grid", *args, **kwargs)
