from spm.__wrapper__ import Runtime


def _prepare_mesh_headshape(*args, **kwargs):
    """
      PREPARE_MESH_HEADSHAPE  
         
        Configuration options should include  
          cfg.headshape   = a filename containing headshape, a Nx3 matrix with surface  
                            points, or a structure with a single or multiple boundaries  
          cfg.smooth      = a scalar indicating the number of non-shrinking  
                            smoothing iterations (default = no smoothing)  
          cfg.numvertices = numeric vector, should have same number of elements as the  
                            number of tissues  
         
        See also PREPARE_MESH_MANUAL, PREPARE_MESH_SEGMENTATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_headshape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_mesh_headshape", *args, **kwargs)
