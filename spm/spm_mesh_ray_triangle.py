from spm._runtime import Runtime


def spm_mesh_ray_triangle(*args, **kwargs):
    r"""
      Compute the intersection of ray(s) and triangle(s)  
        FORMAT [I, t] = spm_mesh_ray_triangle(V, R)  
        V   - double precision matrix of triangles [v1;v2;v3] [9xNV]  
        R   - double precision matrix of rays [origin;direction] [6xNR]   
         
        I   - face indices of intersection hit [NRxN]  
        t   - distance to hit triangles [NRxN]  
       __________________________________________________________________________  
         
        This function implements the Moller-Trumbore ray-triangle intersection  
        algorithm:  
        "Fast, Minimum Storage Ray-Triangle Intersection". Tomas Moller and Ben  
        Trumbore (1997). Journal of Graphics Tools. 2: 21-28.  
        https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm  
        https://fileadmin.cs.lth.se/cs/Personal/Tomas_Akenine-Moller/raytri/  
       __________________________________________________________________________  
         
        This is a low-level function. Please use spm_mesh_ray_intersect.m  
        instead.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_ray_triangle.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_ray_triangle", *args, **kwargs)
