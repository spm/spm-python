from spm.__wrap__ import _Runtime


def spm_ar_freq(*args, **kwargs):
  """  Compute spectra from AR coefficients  
    FORMAT [p] = spm_ar_freq (ar, freq, fs)  
     
    ar    AR model data structure (see spm_ar.m)  
    freq  [Nf x 1] vector containing list of frequencies  
    fs    sample rate  
     
    p     [Nf x 1] vector containing power estimates  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ar_freq.m)
  """

  return _Runtime.call("spm_ar_freq", *args, **kwargs)
