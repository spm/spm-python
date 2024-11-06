from spm.__wrapper__ import Runtime


def _tetrahedron(*args, **kwargs):
    """
      TETRAHEDRON returns the vertices and triangles of a tetraedron  
         
        Use as  
          [pos, tri] = tetrahedron;  
         
        See also ICOSAHEDRON, OCTAHEDRON  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/tetrahedron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tetrahedron", *args, **kwargs)
