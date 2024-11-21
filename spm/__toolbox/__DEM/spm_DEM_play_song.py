from spm.__wrapper__ import Runtime


def spm_DEM_play_song(*args, **kwargs):
    """
      displays the song-bird images specified by the states in qU  
        FORMAT [Y,FS] = spm_DEM_play_song(qU,T);  
         
        qU   - conditional moments of states (see spm_DEM)  
        T    - number of seconds over which to play the sound  
         
        Y    - sound image  
        FS   - sampling rate (Hz)  
         
        A button press on the spectrogram will play the song  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_play_song.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_play_song", *args, **kwargs)
