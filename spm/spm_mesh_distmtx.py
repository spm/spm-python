from spm.__wrapper__ import Runtime


def spm_mesh_distmtx(*args, **kwargs):
    """
      Compute the distance matrix of a triangle mesh  
        FORMAT D = spm_mesh_distmtx(M,order)  
        M        - patch structure  
        order    - 0: adjacency matrix  
                   1: first order distance matrix [default]  
                   2: second order distance matrix  
         
        D        - distance matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_distmtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_distmtx", *args, **kwargs)
