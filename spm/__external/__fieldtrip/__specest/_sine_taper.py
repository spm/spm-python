from spm.__wrapper__ import Runtime


def _sine_taper(*args, **kwargs):
  """  Compute Riedel & Sidorenko sine tapers.  
    sine_taper(n, k) produces the first 2*k tapers of length n,  
    returned as the columns of d.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/sine_taper.m)
  """

  return Runtime.call("sine_taper", *args, **kwargs)
