from spm.__wrap__ import _Runtime


def spm_hilbert(*args, **kwargs):
  """  Computes analytic signal  
    FORMAT [x] = spm_hilbert(xr)  
     
    Returns analytic signal x = xr + i*xi such that xi is the Hilbert  
    transform of real vector xr.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hilbert.m)
  """

  return _Runtime.call("spm_hilbert", *args, **kwargs)
