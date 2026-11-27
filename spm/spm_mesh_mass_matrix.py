from spm._runtime import Runtime


def spm_mesh_mass_matrix(*args, **kwargs):
    r"""
      Compute the mass matrix of a triangle mesh  
        M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
         
        A        - Mass matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_mass_matrix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_mass_matrix", *args, **kwargs)
