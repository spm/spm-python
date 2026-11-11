from spm._runtime import Runtime


def _prepare_mesh_tetrahedral(*args, **kwargs):
    r"""
      PREPARE_MESH_TETRAHEDRAL  
         
        See also PREPARE_MESH_MANUAL, PREPARE_MESH_HEADSHAPE,  
        PREPARE_MESH_HEXAHEDRAL, PREPARE_MESH_SEGMENTATION  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/prepare_mesh_tetrahedral.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_mesh_tetrahedral", *args, **kwargs)
