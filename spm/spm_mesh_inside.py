from spm._runtime import Runtime


def spm_mesh_inside(*args, **kwargs):
    r"""
      Test whether a point is inside or outside a watertight triangle mesh  
        FORMAT T = spm_mesh_inside(M,XYZ)  
        M        - a patch structure or GIfTI object   
        XYZ      - a 1 x 3 vector of point coordinates {mm}  
         
        T        - logical scalar indicating inside/outside mesh test  
       __________________________________________________________________________  
         
        Uses the ray casting algorithm:  
        https://en.wikipedia.org/wiki/Point_in_polygon  
       __________________________________________________________________________  
         
        M = gifti('mesh.gii');  
        M = export(M,'patch');  
         
        m = max(M.vertices,[],1);  
        n = min(M.vertices,[],1);  
        P = (m-n).*rand(4096,3) + n;  
         
        for i=1:size(P,1)  
            T(i) = spm_mesh_inside(M,P(i,:));  
        end  
         
        figure, plot3(P(T,1), P(T,2), P(T,3), '.')  
        H = spm_mesh_render(M);  
        hold(H.axis,'on');  
        plot3(P(T,1), P(T,2), P(T,3), '.','Parent',H.axis)  
        plot3(P(~T,1), P(~T,2), P(~T,3), '.r','Parent',H.axis)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_inside.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_inside", *args, **kwargs)
