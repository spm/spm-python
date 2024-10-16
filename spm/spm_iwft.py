from spm.__wrapper__ import Runtime


def spm_iwft(*args, **kwargs):
  """  Inverse windowed Fourier transform - continuous synthesis  
    FORMAT [s] = spm_iwft(C,k,n);  
    s      - 1-D time-series  
    k      - Frequencies (cycles per window)  
    n      - window length  
    C      - coefficients (complex)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_iwft.m)
  """

  return Runtime.call("spm_iwft", *args, **kwargs)
