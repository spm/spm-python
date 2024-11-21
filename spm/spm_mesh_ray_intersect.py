from spm.__wrapper__ import Runtime


def spm_mesh_ray_intersect(*args, **kwargs):
    """
      Compute the intersection of ray(s) and triangle(s)  
        FORMAT [I, P, t] = spm_mesh_ray_intersect(M, R)  
        M   - a GIfTI object or patch structure or numeric array [v1;v2;v3]  
        R   - ray defined as a structure with fields 'orig' for origin and 'vec'  
              for direction, stored as column vectors  
         
        I   - logical vector indicating intersection hit  
        P   - coordinates of intersections [Mx3]  
        t   - distance to hit triangles  
       __________________________________________________________________________  
         
        This function implements the Moller-Trumbore ray-triangle intersection  
        algorithm:  
        "Fast, Minimum Storage Ray-Triangle Intersection". Tomas Moller and Ben  
        Trumbore (1997). Journal of Graphics Tools. 2: 21-28.  
        https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm  
       __________________________________________________________________________  
         
        M = gifti(fullfile(spm('Dir'),'canonical','scalp_2562.surf.gii'));  
        R = struct('orig',[-100 100 -50]','vec',[150 -250 130]');  
        [I,P] = spm_mesh_ray_intersect(M,R);  
        spm_mesh_render(M);  
        hold on  
        p = plot3([R.orig(1) R.orig(1)+R.vec(1)],...  
            [R.orig(2) R.orig(2)+R.vec(2)],...  
            [R.orig(3) R.orig(3)+R.vec(3)],'-r','LineWidth',4);  
        plot3(P(:,1),P(:,2),P(:,3),'*g','LineWidth',4);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_ray_intersect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_ray_intersect", *args, **kwargs)
