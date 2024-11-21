from spm.__wrapper__ import Runtime


def _mesh_cylinder(*args, **kwargs):
    """
      MESH_CYLINDER creates a triangulated cylinder  
         
        Use as  
          [pnt, tri] = mesh_cylinder(Naz, Nel)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_cylinder.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_cylinder", *args, **kwargs)
