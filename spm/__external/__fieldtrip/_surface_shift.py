from spm.__wrapper__ import Runtime


def _surface_shift(*args, **kwargs):
    """
      SURFACE_SHIFT inflates or deflates a triangulated surface by moving the  
        vertices outward or inward along their normals.  
         
        Use as  
          pos = surface_inflate(pos, tri, amount)  
        where pos and tri describe the surface.  
         
        See also SURFACE_NORMALS, SURFACE_ORIENTATION, SURFACE_INSIDE,  
        SURFACE_NESTING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/surface_shift.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("surface_shift", *args, **kwargs)
