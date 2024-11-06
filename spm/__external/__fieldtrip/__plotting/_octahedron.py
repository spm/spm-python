from spm.__wrapper__ import Runtime


def _octahedron(*args, **kwargs):
    """
      OCTAHEDRON  
         
        Use as  
          [pos tri] = octahedron;  
         
        See also TETRAHEDRON ICOSAHEDRON  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/octahedron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("octahedron", *args, **kwargs)
