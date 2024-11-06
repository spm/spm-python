from spm.__wrapper__ import Runtime


def spm_mesh_polyhedron(*args, **kwargs):
    """
      Return one of the Platonic solids with triangle faces  
        FORMAT M = spm_mesh_polyhedron(name)  
        name     - polyhedron name  
                   (one of {'tetrahedron','octahedron','icosahedron'})  
          
        M        - patch structure  
       __________________________________________________________________________  
         
        See https://www.wikipedia.org/wiki/Platonic_solid  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_polyhedron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_polyhedron", *args, **kwargs)
