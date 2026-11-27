from spm._runtime import Runtime


def spm_mesh_contour(*args, **kwargs):
    r"""
      Compute contour lines of a triangular mesh  
        FORMAT S = spm_mesh_contour(M,z)  
        M   - a GIfTI object or patch structure  
        z   - height of z-plane  
         
        FORMAT S = spm_mesh_contour(M,mat)  
        mat - 4 x 4 transformation matrix  
              (use z-plane at z = 0 after linear transformation according to mat)  
         
        S   - struct array of contour lines with fields 'xdata', 'ydata',  
              'zdata' and 'isopen'  
       __________________________________________________________________________  
         
        figure, hold on, axis equal  
        M = gifti(fullfile(spm('Dir'),'canonical','cortex_20484.surf.gii'));  
        z = linspace(min(M.vertices(:,3)),max(M.vertices(:,3)),20);  
        for i=1:numel(z)  
          S = spm_mesh_contour(M,z(i));  
          for j=1:numel(S)  
            plot3(S(j).xdata,S(j).ydata,S(j).zdata);  
          end  
        end  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_contour.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_contour", *args, **kwargs)
