from spm.__wrapper__ import Runtime


def _combineClusters(*args, **kwargs):
  """  COMBINECLUSTERS is a helper function for FINDCLUSTER. It searches for  
    adjacent clusters in neighbouring channels and combines them.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/combineClusters.m)
  """

  return Runtime.call("combineClusters", *args, **kwargs)
