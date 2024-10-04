from spm.__wrap__ import _Runtime


def _clusterstat(*args, **kwargs):
  """  CLUSTERSTAT computers cluster statistic for multidimensional channel-freq-time or  
    volumetric source data  
     
    See also TFCESTAT, FINDCLUSTER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/clusterstat.m)
  """

  return _Runtime.call("clusterstat", *args, **kwargs)
