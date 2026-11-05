from spm._runtime import Runtime


def spm_mesh_distmtx(*args, **kwargs):
    r"""
      Compute the distance matrix of a triangle mesh  
        FORMAT D = spm_mesh_distmtx(M,order)  
        M        - patch structure  
        order    - 0: adjacency matrix  
                   1: first order distance matrix [default]  
                   2: second order distance matrix  
         
        D        - distance matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_distmtx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_distmtx", *args, **kwargs)
