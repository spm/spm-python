from spm.__wrapper__ import Runtime


def spm_surf(*args, **kwargs):
    """
      Surface extraction  
        FORMAT spm_surf(P,mode,thresh)  
         
        P      - char array of filenames  
                 Usually, this will be c1xxx.<ext> & c2xxx.<ext> - grey and white  
                 matter segments created using the segmentation routine.  
        mode   - operation mode [1: rendering, 2: surface, 3: both]  
        thresh - vector or threshold values for extraction [default: 0.5]  
                 This is only relevant for extracting surfaces, not rendering.  
         
        Generated files (depending on 'mode'):  
        A "render_xxx.mat" file can be produced that can be used for  
        rendering activations on to, see spm_render.  
         
        A "xxx.surf.gii" file can also be written, which is created using  
        Matlab's isosurface function.  
        This extracted brain surface can be viewed using code something like:  
           FV = gifti(spm_select(1,'mesh','Select surface data'));  
           FV = export(FV,'patch');  
           fg = spm_figure('GetWin','Graphics');  
           ax = axes('Parent',fg);  
           p  = patch(FV, 'Parent',ax,...  
                  'FaceColor', [0.8 0.7 0.7], 'FaceVertexCData', [],...  
                  'EdgeColor', 'none',...  
                  'FaceLighting', 'gouraud',...  
                  'SpecularStrength' ,0.7, 'AmbientStrength', 0.1,...  
                  'DiffuseStrength', 0.7, 'SpecularExponent', 10);  
           set(0,'CurrentFigure',fg);  
           set(fg,'CurrentAxes',ax);  
           l  = camlight(-40, 20);   
           axis image;  
           rotate3d on;  
         
        FORMAT out = spm_surf(job)  
          
        Input  
        A job structure with fields  
        .data   - cell array of filenames  
        .mode   - operation mode  
        .thresh - thresholds for extraction  
        Output  
        A struct with fields (depending on operation mode)  
        .rendfile - cellstring containing render filename  
        .surffile - cellstring containing surface filename(s)  
       __________________________________________________________________________  
         
        This surface extraction is not particularly sophisticated.  It simply  
        smooths the data slightly and extracts the surface at a threshold of  
        0.5. The input segmentation images can be manually cleaned up first using  
        e.g., MRIcron.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_surf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_surf", *args, **kwargs)
