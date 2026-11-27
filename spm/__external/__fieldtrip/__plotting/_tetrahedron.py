from spm._runtime import Runtime


def _tetrahedron(*args, **kwargs):
    r"""
      TETRAHEDRON returns the vertices and triangles of a tetraedron  
         
        Use as  
          [pos, tri] = tetrahedron;  
         
        See also ICOSAHEDRON, OCTAHEDRON  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/tetrahedron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tetrahedron", *args, **kwargs)
