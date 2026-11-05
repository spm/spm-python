from spm._runtime import Runtime


def _find_mesh_edge(*args, **kwargs):
    r"""
      FIND_MESH_EDGE returns the edge of a triangulated mesh  
         
        [pnt, line] = find_mesh_edge(pnt, tri), where  
         
        pnt   contains the vertex locations and   
        line  contains the indices of the linepieces connecting the vertices  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/find_mesh_edge.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("find_mesh_edge", *args, **kwargs)
