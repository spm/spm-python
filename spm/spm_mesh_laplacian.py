from spm.__wrapper__ import Runtime


def spm_mesh_laplacian(*args, **kwargs):
    """
      Compute the graph or (cotangent) mesh Laplacian  
        M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
        T        - {'graph','mesh'} [Default: 'graph']  
         
        L        - Laplacian  
       __________________________________________________________________________  
         
        Laplacian matrix:  
          https://en.wikipedia.org/wiki/Laplacian_matrix  
          https://en.wikipedia.org/wiki/Discrete_Laplace_operator#Mesh_Laplacians  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_laplacian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_laplacian", *args, **kwargs)
