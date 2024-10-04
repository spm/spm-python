from spm.__wrap__ import _Runtime


def spm_DEM_play_song(*args, **kwargs):
  """  displays the song-bird images specified by the states in qU  
    FORMAT [Y,FS] = spm_DEM_play_song(qU,T);  
     
    qU   - conditional moments of states (see spm_DEM)  
    T    - number of seconds over which to play the sound  
     
    Y    - sound image  
    FS   - sampling rate (Hz)  
     
    A button press on the spectrogram will play the song  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_play_song.m)
  """

  return _Runtime.call("spm_DEM_play_song", *args, **kwargs)
