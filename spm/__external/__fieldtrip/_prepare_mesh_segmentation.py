from spm.__wrap__ import _Runtime


def _prepare_mesh_segmentation(*args, **kwargs):
  """  PREPARE_MESH_SEGMENTATION  
     
    The following configuration options can be specified for the iso2mesh method  
      cfg.maxsurf     = 1 = only use the largest disjointed surface  
                        0 = use all surfaces for that levelset  
      cfg.radbound    = a scalar indicating the radius of the target surface  
                        mesh element bounding sphere  
     
    See also PREPARE_MESH_MANUAL, PREPARE_MESH_HEADSHAPE, PREPARE_MESH_HEXAHEDRAL,  
    PREPARE_MESH_TETRAHEDRAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_segmentation.m)
  """

  return _Runtime.call("prepare_mesh_segmentation", *args, **kwargs)
