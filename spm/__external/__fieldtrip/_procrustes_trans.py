from spm.__wrap__ import _Runtime


def _procrustes_trans(*args, **kwargs):
  """  PROCRUSTES_TRANS returns the homogenous coordinate transformation matrix  
    that warps the specified input points to the target points.   
     
    Use as  
      [h] = procrustes_trans(input, target)   
    where  
      input   Nx3 matrix with coordinates  
      target  Nx3 matrix with coordinates  
      
    The algorithm used for the calculation of the rotation matrix is knonwn  
    as the Procrustes method. Its use for MEG coordinate transformation has   
    been suggested in Fuchs et al. TBME vol. 42, 1995, p. 416ff.  
      
    See also WARP_OPTIM, HEADCOORDINATES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/procrustes_trans.m)
  """

  return _Runtime.call("procrustes_trans", *args, **kwargs)
