from spm.__wrapper__ import Runtime


def spm_DEM_movie(*args, **kwargs):
    """
      displays a movie and set ButtonDownFunction to play it  
        FORMAT [M] = spm_DEM_movie(qU,S,FPS);  
         
        qU   - conditional moments of states (see spm_DEM) or v  
        S    - .mat file or structure containing  
               S.V   - image modes (V)   
               S.F   - image template (format, for spm_unvec)  
         
        M    - movie array  
        FPS  - Frames per second (Hz)  
         
        A button press on the image will play the movie. The i-th frame is simply S.V*qU.v{1}(:,i)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_movie.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_movie", *args, **kwargs)
