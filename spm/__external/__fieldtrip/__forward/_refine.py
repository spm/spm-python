from spm.__wrapper__ import Runtime


def _refine(*args, **kwargs):
    """
      REFINE a 3D surface that is described by a triangulation  
         
        Use as  
          [pos, tri]          = refine(pos, tri)  
          [pos, tri]          = refine(pos, tri, 'banks')  
          [pos, tri, texture] = refine(pos, tri, 'banks', texture)  
          [pos, tri]          = refine(pos, tri, 'updown', numtri)  
         
        If no method is specified, the default is to refine the mesh globally by bisecting  
        each edge according to the algorithm described in Banks, 1983.  
         
        The Banks method allows the specification of a subset of triangles to be refined  
        according to Banks' algorithm. Adjacent triangles will be gracefully dealt with.  
         
        The alternative 'updown' method refines the mesh a couple of times  
        using Banks' algorithm, followed by a downsampling using the REDUCEPATCH  
        function.  
         
        If the textures of the vertices are specified, the textures for the new  
        vertices are computed  
         
        The Banks method is a memory efficient implementation which remembers the  
        previously inserted vertices. The refinement algorithm executes in linear  
        time with the number of triangles. It is mentioned in  
        http://www.cs.rpi.edu/~flaherje/pdf/fea8.pdf, which also contains the original  
        reference.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/refine.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("refine", *args, **kwargs)
