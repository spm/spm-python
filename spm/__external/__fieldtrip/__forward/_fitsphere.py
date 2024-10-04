from spm.__wrap__ import _Runtime


def _fitsphere(*args, **kwargs):
  """  FITSPHERE fits the centre and radius of a sphere to a set of points  
    using Taubin's method.  
     
    Use as  
          [center,radius] = fitsphere(pnt)  
    where  
      pnt     = Nx3 matrix with the Carthesian coordinates of the surface points  
    and  
      center  = the center of the fitted sphere  
      radius  = the radius of the fitted sphere  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/fitsphere.m)
  """

  return _Runtime.call("fitsphere", *args, **kwargs)
