from spm.__wrapper__ import Runtime


def _freq2cumtapcnt(*args, **kwargs):
  """freq2cumtapcnt is a function.  
      freq = freq2cumtapcnt(freq, fsample)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/freq2cumtapcnt.m)
  """

  return Runtime.call("freq2cumtapcnt", *args, **kwargs)
