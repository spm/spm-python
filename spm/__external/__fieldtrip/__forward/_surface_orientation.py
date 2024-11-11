from spm.__wrapper__ import Runtime


def _surface_orientation(*args, **kwargs):
    """
      SURFACE_ORIENTATION returns the string 'inward' or 'outward' or 'unknown',  
        depending on the surface orientation.  
         
        Use as  
          str = surface_orientation(pos, tri)  
        or  
          str = surface_orientation(pos, tri, ori)  
         
        See also SURFACE_AREA, SURFACE_NESTING, SURFACE_NORMALS, SURFACE_NESTING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/surface_orientation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("surface_orientation", *args, **kwargs)
