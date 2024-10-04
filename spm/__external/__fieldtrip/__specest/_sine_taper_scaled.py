from spm.__wrap__ import _Runtime


def _sine_taper_scaled(*args, **kwargs):
  """  Compute Riedel & Sidorenko sine tapers.  
    sine_taper_scaled(n, k) produces the first 2*k tapers of length n,  
    returned as the columns of d. The norm of the tapers will not be 1. The  
    norm is a function of the number of the taper in the sequence. This is to  
    mimick behavior of the scaling of the resulting powerspectra prior to  
    april 29, 2011. Before april 29, 2011, equivalent scaling was applied to  
    the powerspectra of the tapered data segments, prior to averaging.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/sine_taper_scaled.m)
  """

  return _Runtime.call("sine_taper_scaled", *args, **kwargs)
