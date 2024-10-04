from spm.__wrap__ import _Runtime


def spm_s2csd(*args, **kwargs):
  """  Convert eigenspectrum to cross spectral density  
    FORMAT [csd,Hz] = spm_s2csd(s,Hz)  
     
    s    (m x 1}        - eigenspectrum  
    Hz   (n x 1)        - vector of frequencies (Hz)  
     
    csd  (n,m)          - spectral density (of modes)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_s2csd.m)
  """

  return _Runtime.call("spm_s2csd", *args, **kwargs)
