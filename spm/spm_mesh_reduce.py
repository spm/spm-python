from spm.__wrapper__ import Runtime


def spm_mesh_reduce(*args, **kwargs):
    """
      Reduce the number of triangles in a mesh  
        FORMAT M = spm_mesh_reduce(M,f)  
        M        - a patch structure  
        t        - desired number of triangles  
         
        M        - reduced patch structure  
       __________________________________________________________________________  
         
        References:  
         
        M. Garland and P. Heckbert. Surface Simplification Using Quadric Error  
        Metrics. In Proceedings of SIGGRAPH 97.  
        http://mgarland.org/files/papers/quadrics.pdf  
          
        M. Garland and P. Heckbert. Simplifying Surfaces with Color and Texture  
        using Quadric Error Metrics. In Proceedings of IEEE Visualization 98.   
        http://mgarland.org/files/papers/quadric2.pdf  
          
        Wrapper around a C++ implementation by Sven Forstmann, MIT licence:  
        https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification  
        ported to pure C by Chris Rorden, BSD 2-Clause License:  
        https://github.com/neurolabusc/nii2mesh  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_reduce.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_reduce", *args, **kwargs)
