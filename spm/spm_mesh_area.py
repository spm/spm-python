from spm.__wrap__ import _Runtime


def spm_mesh_area(*args, **kwargs):
  """  Compute the surface area of a triangle mesh  
    FORMAT A = spm_mesh_area(M,P)  
    M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
               or 3xm array of edge distances  
    P        - return overall surface area, or per face, or per vertex  
               one of {'sum','face','vertex'} [default: 'sum']  
     
    A        - surface area  
   __________________________________________________________________________  
     
    Computed using numerically stable version of Heron's formula:  
    See https://www.wikipedia.org/wiki/Heron%27s_formula  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_area.m)
  """

  return _Runtime.call("spm_mesh_area", *args, **kwargs)
