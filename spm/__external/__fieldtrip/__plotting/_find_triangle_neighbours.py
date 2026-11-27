from spm._runtime import Runtime


def _find_triangle_neighbours(*args, **kwargs):
    r"""
      FIND_TRIANGLE_NEIGHBOURS determines the three neighbours for each triangle  
        in a mesh. It returns NaN's if the triangle does not have a neighbour on   
        that particular side.  
          
        [nb] = find_triangle_neighbours(pnt, tri)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/find_triangle_neighbours.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("find_triangle_neighbours", *args, **kwargs)
