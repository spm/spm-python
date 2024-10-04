from spm.__wrap__ import _Runtime


def _current_dipole(*args, **kwargs):
  """  CURRENT_DIPOLE leadfield for a current dipole in an infinite homogenous medium  
     
    [lf] = current_dipole(R, pos, ori)  
     
    with input arguments  
      R           position dipole  
      pos         position magnetometers  
      ori         orientation magnetometers  
     
    This implements equation 9.3-1 from R.M. Gulrajani (1998) Bioelectricity and  
    Biomagnetism, John Wiley and Sons, ISBN 04712485252.  
     
    See also MAGNETIC_DIPOLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/current_dipole.m)
  """

  return _Runtime.call("current_dipole", *args, **kwargs)
