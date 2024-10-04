from spm.__wrap__ import _Runtime


def spm_voice_dct(*args, **kwargs):
  """  Logarithmically sampled discrete cosine transform matrix  
    FORMAT [U] = spm_voice_dct(N,K,n,[s])  
     
     N         - dimension  
     K         - order  
     n         - log scaling parameter (typically 4)  
     s         - optional linear scaling [default 1]  
     
    This routine returns a discrete cosine transform matrix sampled  
    logarithmically according to a scaling parameter.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_dct.m)
  """

  return _Runtime.call("spm_voice_dct", *args, **kwargs)
