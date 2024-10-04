from spm.__wrap__ import _Runtime


def spm_morlet_conv(*args, **kwargs):
  """  Temporal convolution of complex spectral responses with Morlet envelope  
    FORMAT [G] = spm_morlet_conv(G,w,dt,wnum)  
     
    G      - (t x w x n x n) cross spectral density  
    w      - Frequencies (Hz)  
    dt     - sampling interval (sec)  
    wnum   - Wavelet number: default = 2  s.d. = wnum/(2*pi*w)  
     
    G      - convolved cross spectral density  
   __________________________________________________________________________  
     
    This routine simply smooths a cross spectral response to emulate a   
    wavelet transform.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_morlet_conv.m)
  """

  return _Runtime.call("spm_morlet_conv", *args, **kwargs)
