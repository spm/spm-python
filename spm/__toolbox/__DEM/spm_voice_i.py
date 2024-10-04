from spm.__wrap__ import _Runtime


def spm_voice_i(*args, **kwargs):
  """  Get indices, word strings or priors from lexicon  
    FORMAT [str] = spm_voice_i(i)  
    FORMAT [i  ] = spm_voice_i(str)  
    FORMAT [i,P] = spm_voice_i(str)  
     
    str  - string or cell array  
    i    - index in lexicon (VOX.LEX)  
    P    - corresponding array of prior probabilities  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_i.m)
  """

  return _Runtime.call("spm_voice_i", *args, **kwargs)
