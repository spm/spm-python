from spm.__wrapper__ import Runtime


def spm_mesh_isoline(*args, **kwargs):
    """
      Compute isolines on a triangular mesh  
        FORMAT C = spm_mesh_isoline(M, T, t)  
        M   - a GIfTI object or patch structure  
        T   - [vx1] data vector  
        t   - isovalue [Default: 0]  
         
        C   - struct array of isolines with fields 'xdata', 'ydata', 'zdata' and  
              'isopen'  
       __________________________________________________________________________  
         
        M = gifti(fullfile(spm('Dir'),'canonical','cortex_20484.surf.gii'));  
        M = export(M,'patch');  
        M = spm_mesh_inflate(M);  
        T = randn(size(M.vertices,1),1);  
        T = spm_mesh_smooth(M,T,100);  
        H = spm_mesh_render('Disp',M);  
        H = spm_mesh_render('Overlay',H,T);  
        hold on  
        t = linspace(min(T),max(T),20);  
        for i=1:numel(t)  
          C = spm_mesh_isoline(M,T,t(i));  
          for j=1:numel(C)  
            plot3(C(j).xdata,C(j).ydata,C(j).zdata,'k-');  
          end  
        end  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_isoline.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_isoline", *args, **kwargs)
