from spm.__wrap__ import _Runtime


def _loadama(*args, **kwargs):
  """  LOADAMA read an inverted A-matrix and associated geometry information  
    from an ama file that was written by Tom Oostendorp's DIPOLI  
     
    Use as  
      [ama] = loadama(filename)  
     
    See also LOADTRI, LOADMAT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/loadama.m)
  """

  return _Runtime.call("loadama", *args, **kwargs)
