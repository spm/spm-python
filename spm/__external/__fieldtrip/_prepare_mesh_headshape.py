from spm._runtime import Runtime


def _prepare_mesh_headshape(*args, **kwargs):
    r"""
      PREPARE_MESH_HEADSHAPE  
         
        Configuration options should include  
          cfg.headshape   = a filename containing headshape, a Nx3 matrix with surface  
                            points, or a structure with a single or multiple boundaries  
          cfg.smooth      = a scalar indicating the number of non-shrinking  
                            smoothing iterations (default = no smoothing)  
          cfg.numvertices = numeric vector, should have same number of elements as the  
                            number of tissues  
         
        See also PREPARE_MESH_MANUAL, PREPARE_MESH_SEGMENTATION  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/prepare_mesh_headshape.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_mesh_headshape", *args, **kwargs)
