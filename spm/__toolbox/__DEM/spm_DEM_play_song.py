from spm._runtime import Runtime


def spm_DEM_play_song(*args, **kwargs):
    r"""
      displays the song-bird images specified by the states in qU  
        FORMAT [Y,FS] = spm_DEM_play_song(qU,T);  
         
        qU   - conditional moments of states (see spm_DEM)  
        T    - number of seconds over which to play the sound  
         
        Y    - sound image  
        FS   - sampling rate (Hz)  
         
        A button press on the spectrogram will play the song  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_DEM_play_song.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_play_song", *args, **kwargs)
