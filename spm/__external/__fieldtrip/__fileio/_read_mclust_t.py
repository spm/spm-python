from spm.__wrap__ import _Runtime


def _read_mclust_t(*args, **kwargs):
  """  adapted from M-clust function LoadSpikes  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mclust_t.m)
  """

  return _Runtime.call("read_mclust_t", *args, **kwargs)
