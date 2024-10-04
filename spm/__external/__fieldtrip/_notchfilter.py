from spm.__wrap__ import _Runtime


def _notchfilter(*args, **kwargs):
  """  NOTCHFILTER line noise reduction filter for EEG/MEG data  
     
    [filt] = notchfilter(dat, Fsample, Fline)  
     
    where  
      dat        data matrix (Nchans X Ntime)  
      Fsample    sampling frequency in Hz  
      Fline      line noise frequency (would normally be 50Hz)  
      N          optional filter order, default is 4  
     
    if Fline is specified as 50, a band of 48-52 is filtered out  
    if Fline is specified as [low high], that band is filtered out  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/notchfilter.m)
  """

  return _Runtime.call("notchfilter", *args, **kwargs)
