from spm.__wrap__ import _Runtime


def spm_mesh(*args, **kwargs):
  """  Load mesh file(s) into memory as patch structure  
    FORMAT M = spm_mesh(meshfilename1,meshfilename2,...)  
     
    M        - patch structure array (.faces and .vertices)   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh.m)
  """

  return _Runtime.call("spm_mesh", *args, **kwargs)
