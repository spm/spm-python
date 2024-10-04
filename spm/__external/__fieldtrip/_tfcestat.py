from spm.__wrap__ import _Runtime


def _tfcestat(*args, **kwargs):
  """  TFCESTAT computes threshold-free cluster statistic multidimensional channel-freq-time or  
    volumetric source data  
     
    See also CLUSTERSTAT, FINDCLUSTER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/tfcestat.m)
  """

  return _Runtime.call("tfcestat", *args, **kwargs)
