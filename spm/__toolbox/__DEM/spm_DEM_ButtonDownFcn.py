from spm.__wrapper__ import Runtime


def spm_DEM_ButtonDownFcn(*args, **kwargs):
  """  ButtonDownFcn to play (or save) a movie or sound on button press  
    FORMAT spm_DEM_ButtonDownFcn  
     
    Requires gcbo to have appropriate UserData; see spm_DEM_movie and  
    spm_DEM_play_song  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_ButtonDownFcn.m)
  """

  return Runtime.call("spm_DEM_ButtonDownFcn", *args, **kwargs, nargout=0)
