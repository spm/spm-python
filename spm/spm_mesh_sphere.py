from spm._runtime import Runtime


def spm_mesh_sphere(*args, **kwargs):
    r"""
      Return a triangle mesh of a unit sphere  
        N        - number of subdivision iterations [Default: 5]  
        M        - initial triangle mesh [Default: 'icosahedron']  
         
        M        - patch structure  
       __________________________________________________________________________  
         
        Computed using geodesic subdivisions of an icosahedron.  
        See https://www.wikipedia.org/wiki/Geodesic_polyhedron  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_sphere.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_sphere", *args, **kwargs)
