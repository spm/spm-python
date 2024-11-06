from spm.__wrapper__ import Runtime


def spm_mesh_bounding_volume(*args, **kwargs):
    """
      Bounding volume of a triangle mesh  
        FORMAT bv = spm_mesh_bounding_volume(M,t)  
        M        - a patch structure or GIfTI object  
        t        - type of bounding volume [default: 'AABB']  
         
        bv       - bounding volume  
       __________________________________________________________________________  
         
        See: https://en.wikipedia.org/wiki/Bounding_volume  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_bounding_volume.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_bounding_volume", *args, **kwargs)
