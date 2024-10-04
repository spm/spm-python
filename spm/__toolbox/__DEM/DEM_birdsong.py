from spm.__wrap__ import _Runtime


def DEM_birdsong(*args, **kwargs):
  """  Create basis set for sounds  
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
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_birdsong.m)
  """

  return _Runtime.call("DEM_birdsong", *args, **kwargs)
