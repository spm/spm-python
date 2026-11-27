from spm._runtime import Runtime


def _surface_area(*args, **kwargs):
    r"""
      SURFACE_AREA computes the surface area of each of the triangles in a mesh  
         
        Use as  
          area = surface_area(pos, tri)  
         
        See also SURFACE_ORIENTATION, SURFACE_INSIDE, SURFACE_NESTING, PROJECTTRI, PCNORMALS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/surface_area.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("surface_area", *args, **kwargs)
