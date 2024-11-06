from spm.__wrapper__ import Runtime


def spm_mesh_mass_matrix(*args, **kwargs):
    """
      Compute the mass matrix of a triangle mesh  
        M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
         
        A        - Mass matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_mass_matrix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_mass_matrix", *args, **kwargs)
