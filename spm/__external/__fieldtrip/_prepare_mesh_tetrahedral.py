from mpython import Runtime


def _prepare_mesh_tetrahedral(*args, **kwargs):
    """
      PREPARE_MESH_TETRAHEDRAL

        See also PREPARE_MESH_MANUAL, PREPARE_MESH_HEADSHAPE,
        PREPARE_MESH_HEXAHEDRAL, PREPARE_MESH_SEGMENTATION


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_tetrahedral.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_mesh_tetrahedral", *args, **kwargs)
