from spm.__wrapper__ import Runtime


def spm_mesh_adjacency(*args, **kwargs):
    """
      Compute the adjacency matrix of a triangle mesh  
        FORMAT A = spm_mesh_adjacency(F)  
        F        - a [fx3] faces array or a patch structure  
          
        A        - adjacency matrix as a sparse [vxv] array  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_adjacency.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_adjacency", *args, **kwargs)
