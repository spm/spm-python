from spm.__wrapper__ import Runtime


def _find_mesh_edge(*args, **kwargs):
    """
      FIND_MESH_EDGE returns the edge of a triangulated mesh  
         
        [pnt, line] = find_mesh_edge(pnt, tri), where  
         
        pnt   contains the vertex locations and   
        line  contains the indices of the linepieces connecting the vertices  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/find_mesh_edge.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("find_mesh_edge", *args, **kwargs)
