from spm._runtime import Runtime


def _remove_vertices(*args, **kwargs):
    r"""
      REMOVE_VERTICES removes specified indexed vertices from a triangular, tetrahedral  
        or hexahedral mesh renumbering the vertex-indices for the elements and removing all  
        resulting 'open' elements.  
         
        Use as  
          [pos, tri] = remove_vertices(pos, tri, sel)  
          [pos, tet] = remove_vertices(pos, tet, sel)  
          [pos, hex] = remove_vertices(pos, hex, sel)  
         
        See also REMOVE_DOUBLE_VERTICES, REMOVE_UNUSED_VERTICES  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/remove_vertices.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("remove_vertices", *args, **kwargs)
