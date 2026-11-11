from spm._runtime import Runtime


def spm_mesh_polyhedron(*args, **kwargs):
    r"""
      Return one of the Platonic solids with triangle faces  
        FORMAT M = spm_mesh_polyhedron(name)  
        name     - polyhedron name  
                   (one of {'tetrahedron','octahedron','icosahedron'})  
          
        M        - patch structure  
       __________________________________________________________________________  
         
        See https://www.wikipedia.org/wiki/Platonic_solid  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_polyhedron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_polyhedron", *args, **kwargs)
