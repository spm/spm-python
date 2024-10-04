from spm.__wrap__ import _Runtime


def DEM_demo_song_priors(*args, **kwargs):
  """  Demo for a bird songs: In this example, we simulate local field potential  
    using the prediction error from the song-bird example below. We look at  
    these responses under natural stimuli and after removing the second  
    level of the hierarchy to show it is necessary for veridical perception.  
    We then repeat but omitting dynamical priors by forsaking generalised   
    coordinates  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_song_priors.m)
  """

  return _Runtime.call("DEM_demo_song_priors", *args, **kwargs, nargout=0)
