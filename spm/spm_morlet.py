from spm.__wrapper__ import Runtime


def spm_morlet(*args, **kwargs):
  """  Morlet wavelet transform (time-frequency analysis)  
    FORMAT [C] = spm_morlet(s,k,wnum)  
     
    s      - (t X n) time-series  
    k      - Frequencies (cycles per time bin)  
    wnum   - Wavelet number: default = 6  
     
    C      - coefficients (complex)  
   __________________________________________________________________________  
     
    This routine returns a Morlet-like wavelet transform but uses a Hanning  
    window, as opposed to a Gaussian window.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_morlet.m)
  """

  return Runtime.call("spm_morlet", *args, **kwargs)
