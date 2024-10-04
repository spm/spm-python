from spm.__wrap__ import _Runtime


def _freq2cumtapcnt(*args, **kwargs):
  """freq2cumtapcnt is a function.  
      freq = freq2cumtapcnt(freq, fsample)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/freq2cumtapcnt.m)
  """

  return _Runtime.call("freq2cumtapcnt", *args, **kwargs)
