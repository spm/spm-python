from spm.__wrap__ import _Runtime


def spm_voice_onsets(*args, **kwargs):
  """  Identify intervals containing acoustic energy and post onset minima  
    FORMAT [I] = spm_voice_onsets(Y,FS,C,U)  
     
    Y    - timeseries  
    FS   - sampling frequency  
    C    - Convolution kernel [Default: 1/16 sec]  
    U    - crossing threshold [Default: 1/8  a.u]  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_onsets.m)
  """

  return _Runtime.call("spm_voice_onsets", *args, **kwargs)
