from spm.__wrapper__ import Runtime


def _prepare_mesh_hexahedral(*args, **kwargs):
    """
      PREPARE_MESH_HEXAHEDRAL  
         
        Configuration options for generating a regular 3-D grid  
          cfg.tissue     = cell with the names of the compartments that should be meshed  
          cfg.shift  
          cfg.background  
         
        See also PREPARE_MESH_SEGMENTATION, PREPARE_MESH_MANUAL, PREPARE_MESH_HEADSHAPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_hexahedral.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_mesh_hexahedral", *args, **kwargs)
