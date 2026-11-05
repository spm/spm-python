from spm._runtime import Runtime


def _prepare_mesh_fittemplate(*args, **kwargs):
    r"""
      PREPARE_MESH_FITTEMPLATE computes an affine transformation matrix between 2 point clouds   
         
        This function relies on cpd toolbox from  Myronenko, see https://sites.google.com/site/myronenko/research/cpd  
         
        See also FT_PREPARE_MESH  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/prepare_mesh_fittemplate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_mesh_fittemplate", *args, **kwargs)
