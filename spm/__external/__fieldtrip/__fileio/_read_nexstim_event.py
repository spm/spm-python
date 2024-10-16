from spm.__wrapper__ import Runtime


def _read_nexstim_event(*args, **kwargs):
  """  Use as  
      [event] = read_nexstim_event(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nexstim_event.m)
  """

  return Runtime.call("read_nexstim_event", *args, **kwargs)
