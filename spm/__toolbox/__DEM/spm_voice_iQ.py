from spm.__wrapper__ import Runtime


def spm_voice_iQ(*args, **kwargs):
  """  Discrete cosine transform of formant coefficients  
    FORMAT [W] = spm_voice_iQ(Q)  
     
    Q     - log formant frequencies  
    G(1)  - log formant (pitch) Tu  
    G(2)  - log timing  (pitch) Tv  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_iQ.m)
  """

  return Runtime.call("spm_voice_iQ", *args, **kwargs)
