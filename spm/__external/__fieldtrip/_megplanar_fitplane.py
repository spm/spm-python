from spm.__wrap__ import _Runtime


def _megplanar_fitplane(*args, **kwargs):
  """  Fit a plane through the B=f(x,y) plane and compute its two gradients  
    The first point in the plane is the gradiometer itself,  
    the neighbours are the subsequent points. This method also returns the  
    offset of the B-plane at each sensor, which is appriximately equal to the  
    field itself.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_fitplane.m)
  """

  return _Runtime.call("megplanar_fitplane", *args, **kwargs)
