from spm._runtime import Runtime


def spm_mesh_laplacian(*args, **kwargs):
    r"""
      Compute the graph or (cotangent) mesh Laplacian  
        M        - patch structure: vertices and faces must be mx3 and nx3 arrays  
        T        - {'graph','mesh'} [Default: 'graph']  
         
        L        - Laplacian  
       __________________________________________________________________________  
         
        Laplacian matrix:  
          https://en.wikipedia.org/wiki/Laplacian_matrix  
          https://en.wikipedia.org/wiki/Discrete_Laplace_operator#Mesh_Laplacians  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_laplacian.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_laplacian", *args, **kwargs)
