from spm.__wrap__ import _Runtime


def hilbert(*args, **kwargs):
  """  Computes analytic signal  
    FORMAT [x] = hilbert(xr)  
     
    Returns analytic signal x = xr + i*xi such that   
    xi is the Hilbert transform of real vector xr.  
   __________________________________________________________________________  
    Copyright (C) 2009 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/hilbert.m)
  """

  return _Runtime.call("hilbert", *args, **kwargs)
