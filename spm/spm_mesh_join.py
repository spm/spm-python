from spm.__wrapper__ import Runtime


def spm_mesh_join(*args, **kwargs):
    """
      Join a list of surface meshes into a single one  
        FORMAT [M, I] = spm_mesh_join(Ms)  
        Ms            - a patch structure array or list of scalar patch structures  
         
        M             - a scalar patch structure  
        I             - a column vector of face indices  
         
        See also spm_mesh_split  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_join.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_join", *args, **kwargs)
