from spm.__wrapper__ import Runtime


def _prepare_mesh_fittemplate(*args, **kwargs):
  """  PREPARE_MESH_FITTEMPLATE computes an affine transformation matrix between 2 point clouds   
     
    This function relies on cpd toolbox from  Myronenko, see https://sites.google.com/site/myronenko/research/cpd  
     
    See also FT_PREPARE_MESH  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_fittemplate.m)
  """

  return Runtime.call("prepare_mesh_fittemplate", *args, **kwargs)
