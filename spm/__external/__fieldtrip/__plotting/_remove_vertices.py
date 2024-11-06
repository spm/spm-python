from spm.__wrapper__ import Runtime


def _remove_vertices(*args, **kwargs):
    """
      REMOVE_VERTICES removes specified indexed vertices from a triangular, tetrahedral  
        or hexahedral mesh renumbering the vertex-indices for the elements and removing all  
        resulting 'open' elements.  
         
        Use as  
          [pos, tri] = remove_vertices(pos, tri, sel)  
          [pos, tet] = remove_vertices(pos, tet, sel)  
          [pos, hex] = remove_vertices(pos, hex, sel)  
         
        See also REMOVE_DOUBLE_VERTICES, REMOVE_UNUSED_VERTICES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/remove_vertices.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("remove_vertices", *args, **kwargs)
