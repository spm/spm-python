from spm.__wrapper__ import Runtime


def spm_mesh_cube(*args, **kwargs):
    """
      Triangle mesh of a unit cube  
        FORMAT M = spm_mesh_cube  
        M        - patch structure  
       __________________________________________________________________________  
         
        Return a triangle mesh of a unit cube (sides of 1 unit long).  
        See https://www.wikipedia.org/wiki/Unit_cube  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_cube.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_cube", *args, **kwargs)
