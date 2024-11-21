from spm.__wrapper__ import Runtime


def _find_vertex_neighbours(*args, **kwargs):
    """
      FIND_VERTEX_NEIGHBOURS determines the neighbours of a specified vertex  
        in a mesh.  
          
        [nb] = find_vertex_neighbours(pnt, tri, indx)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/find_vertex_neighbours.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("find_vertex_neighbours", *args, **kwargs)
