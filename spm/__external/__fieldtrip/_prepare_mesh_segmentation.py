from spm._runtime import Runtime


def _prepare_mesh_segmentation(*args, **kwargs):
    r"""
      PREPARE_MESH_SEGMENTATION  
         
        The following configuration options can be specified for the iso2mesh method  
          cfg.maxsurf     = 1 = only use the largest disjointed surface  
                            0 = use all surfaces for that levelset  
          cfg.radbound    = a scalar indicating the radius of the target surface  
                            mesh element bounding sphere  
         
        See also PREPARE_MESH_MANUAL, PREPARE_MESH_HEADSHAPE, PREPARE_MESH_HEXAHEDRAL,  
        PREPARE_MESH_TETRAHEDRAL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/prepare_mesh_segmentation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_mesh_segmentation", *args, **kwargs)
