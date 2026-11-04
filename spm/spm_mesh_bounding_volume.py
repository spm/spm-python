from spm._runtime import Runtime


def spm_mesh_bounding_volume(*args, **kwargs):
    r"""
      Bounding volume of a triangle mesh  
        FORMAT bv = spm_mesh_bounding_volume(M,t)  
        M        - a patch structure or GIfTI object  
        t        - type of bounding volume [default: 'AABB']  
         
        bv       - bounding volume  
       __________________________________________________________________________  
         
        See: https://en.wikipedia.org/wiki/Bounding_volume  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_bounding_volume.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_bounding_volume", *args, **kwargs)
