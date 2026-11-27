from spm._runtime import Runtime


def _surface_orientation(*args, **kwargs):
    r"""
      SURFACE_ORIENTATION returns the string 'inward' or 'outward' or 'unknown',  
        depending on the surface orientation.  
         
        Use as  
          str = surface_orientation(pos, tri)  
        or  
          str = surface_orientation(pos, tri, ori)  
         
        See also SURFACE_AREA, SURFACE_NESTING, SURFACE_NORMALS, SURFACE_NESTING  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/surface_orientation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("surface_orientation", *args, **kwargs)
