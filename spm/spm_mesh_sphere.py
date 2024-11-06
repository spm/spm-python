from spm.__wrapper__ import Runtime


def spm_mesh_sphere(*args, **kwargs):
    """
      Return a triangle mesh of a unit sphere  
        N        - number of subdivision iterations [Default: 5]  
        M        - initial triangle mesh [Default: 'icosahedron']  
         
        M        - patch structure  
       __________________________________________________________________________  
         
        Computed using geodesic subdivisions of an icosahedron.  
        See https://www.wikipedia.org/wiki/Geodesic_polyhedron  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_sphere.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_sphere", *args, **kwargs)
