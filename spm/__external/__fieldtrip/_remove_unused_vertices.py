from spm._runtime import Runtime


def _remove_unused_vertices(*args, **kwargs):
    """
      REMOVE_UNUSED_VERTICES removes unused vertices from a triangular, tetrahedral or  
        hexahedral mesh, renumbering the vertex-indices for the elements.  
         
        Use as  
          [pos, tri] = remove_unused_vertices(pos, tri)  
          [pos, tet] = remove_unused_vertices(pos, tet)  
          [pos, hex] = remove_unused_vertices(pos, hex)  
         
        See also REMOVE_VERTICES, REMOVE_DOUBLE_VERTICES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/remove_unused_vertices.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("remove_unused_vertices", *args, **kwargs)
