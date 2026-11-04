from spm._runtime import Runtime


def _mesh_cylinder(*args, **kwargs):
    r"""
      MESH_CYLINDER creates a triangulated cylinder  
         
        Use as  
          [pnt, tri] = mesh_cylinder(Naz, Nel)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/mesh_cylinder.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_cylinder", *args, **kwargs)
