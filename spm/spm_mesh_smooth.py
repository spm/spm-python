from spm.__wrapper__ import Runtime


def spm_mesh_smooth(*args, **kwargs):
    """
      Perform Gaussian smoothing on data lying on a surface mesh  
        FORMAT K = spm_mesh_smooth(M)  
        M        - patch structure  
        K        - smoothing kernel (based on graph Laplacian)  
         
        FORMAT T = spm_mesh_smooth(M, T, S)  
        FORMAT T = spm_mesh_smooth(K, T, S)  
        T        - [vx1] data vector  
        S        - smoothing parameter (number of iterations)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_smooth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_smooth", *args, **kwargs)
