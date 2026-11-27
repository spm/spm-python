from spm._runtime import Runtime


def spm_mesh_adjacency(*args, **kwargs):
    r"""
      Compute the adjacency matrix of a triangle mesh  
        FORMAT A = spm_mesh_adjacency(F)  
        F        - a [fx3] faces array or a patch structure  
          
        A        - adjacency matrix as a sparse [vxv] array  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_adjacency.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_adjacency", *args, **kwargs)
