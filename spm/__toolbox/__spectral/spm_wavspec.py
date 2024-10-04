from spm.__wrap__ import _Runtime


def spm_wavspec(*args, **kwargs):
  """  Wavelet based spectrogram  
    FORMAT [p] = spm_wavspec (x,freqs,fs,show,rtf)  
    x         Data vector  
    freqs     Frequencies to estimate power at  
    fs        sample rate  
    show      1 to plot real part of wavelet basis used (default = 0)  
    rtf       Wavelet factor (if > 10, then this parameter defaults to a   
              fixed window length of rtf milliseconds)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_wavspec.m)
  """

  return _Runtime.call("spm_wavspec", *args, **kwargs)
