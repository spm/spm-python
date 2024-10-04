from spm.__wrap__ import _Runtime


def _GALA_clustering(*args, **kwargs):
  """GALA_clustering is a function.  
      res = GALA_clustering(lJcov, J1, S, distance, A)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_clustering.m)
  """

  return _Runtime.call("GALA_clustering", *args, **kwargs)
