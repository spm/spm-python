from spm._runtime import Runtime


def spm_mesh_cube(*args, **kwargs):
    r"""
      Triangle mesh of a unit cube  
        FORMAT M = spm_mesh_cube  
        M        - patch structure  
       __________________________________________________________________________  
         
        Return a triangle mesh of a unit cube (sides of 1 unit long).  
        See https://www.wikipedia.org/wiki/Unit_cube  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_cube.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_cube", *args, **kwargs)
