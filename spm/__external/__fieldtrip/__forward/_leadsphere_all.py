from spm.__wrapper__ import Runtime


def _leadsphere_all(*args, **kwargs):
  """  usage: out=leadsphere_all(xloc,sensorloc,sensorori)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadsphere_all.m)
  """

  return Runtime.call("leadsphere_all", *args, **kwargs)
