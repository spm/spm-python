from spm.__wrap__ import _Runtime


def _freq2timelock(*args, **kwargs):
  """  FREQ2TIMELOCK  transform the frequency data into something  
    on which the timelocked source reconstruction methods can  
    perform their trick.  
     
    This function also performs frequency and channel selection, using  
      cfg.frequency  
      cfg.channel  
     
    After source reconstruction, you should use TIMELOCK2FREQ.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/freq2timelock.m)
  """

  return _Runtime.call("freq2timelock", *args, **kwargs)
