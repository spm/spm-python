from spm._runtime import Runtime


def DEM_birdsong(*args, **kwargs):
    r"""
      Create basis set for sounds  
        FORMAT [S] = DEM_birdsong(file)  
         
        file  - .wav file  
         
        S.U   - h x 3 basis functions (Hz)  
        S.V   - 3 x n basis functions (seconds)  
        S.Hz  - s x 1 frequencies (Hz)  
         
        Bird Song demo: These simple loads a .wav file of a real bird-song; and  
        approximates the ensuing spectrogram with in terms of three  
        time-frequency modes.  These modes are saved in BirdSong.mat (U) for  
        illustrating DEM_demo_sequences  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_birdsong.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_birdsong", *args, **kwargs)
