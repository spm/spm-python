from spm.__wrap__ import _Runtime


def _sphericalSplineInterpolate(*args, **kwargs):
  """ interpolate matrix for spherical interpolation  
     
    W = sphericalSplineInterpolate(src,dest,lambda,order,type,tol)  
     
    Inputs:  
     src    - [3 x N] old electrode positions  
     dest   - [3 x M] new electrode positions  
     lambda - [float] regularisation parameter for smoothing the estimates (1e-5)  
     order  - [float] order of the polynomial interplotation to use (4)  
     type - [str] one of;                                         ('spline')  
                'spline' - spherical Spline   
                'slap'   - surface Laplician (aka. CSD)  
     tol    - [float] tolerance for the legendre poly approx        (1e-7)  
    Outputs:  
     W      - [M x N] linear mapping matrix between old and new co-ords  
     
    Based upon the paper: Perrin89  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/sphericalSplineInterpolate.m)
  """

  return _Runtime.call("sphericalSplineInterpolate", *args, **kwargs)
