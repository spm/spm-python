from spm.__wrapper__ import Runtime


def _find_triangle_neighbours(*args, **kwargs):
    """
      FIND_TRIANGLE_NEIGHBOURS determines the three neighbours for each triangle  
        in a mesh. It returns NaN's if the triangle does not have a neighbour on   
        that particular side.  
          
        [nb] = find_triangle_neighbours(pnt, tri)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/find_triangle_neighbours.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("find_triangle_neighbours", *args, **kwargs)
