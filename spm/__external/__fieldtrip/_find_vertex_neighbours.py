from spm._runtime import Runtime


def _find_vertex_neighbours(*args, **kwargs):
    r"""
      FIND_VERTEX_NEIGHBOURS determines the neighbours of a specified vertex  
        in a mesh.  
          
        [nb] = find_vertex_neighbours(pnt, tri, indx)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/find_vertex_neighbours.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("find_vertex_neighbours", *args, **kwargs)
