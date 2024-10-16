from spm.__wrapper__ import Runtime


def spm_beamforming(*args, **kwargs):
  """  GUI gateway to Beamforming toolbox  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/spm_beamforming.m)
  """

  return Runtime.call("spm_beamforming", *args, **kwargs, nargout=0)
