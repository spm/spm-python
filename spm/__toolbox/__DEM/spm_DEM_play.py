from spm.__wrapper__ import Runtime


def spm_DEM_play(*args, **kwargs):
    """
      displays the sound images specified by the states in qU  
        FORMAT [Y,FS] = spm_DEM_play(qU,S,T);  
         
        qU   - conditional moments of states (see spm_DEM)  
        S    - .mat file or structure   
               U.U   - containing frequency modes (U)   
               S.Hz  - and corresponding frequencies (FS)  
        T    - number of second over which to play the sound  
         
        Y    - sound image  
        FS   - sampling rate (Hz)  
         
        A button press on the spectrogram will play the sound  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_play.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_play", *args, **kwargs)
