from spm.__wrapper__ import Runtime


def _magnetic_dipole(*args, **kwargs):
  """  MAGNETIC_DIPOLE leadfield for a magnetic dipole in an infinite medium  
     
    [lf] = magnetic_dipole(R, pos, ori)  
     
    with input arguments  
      R           position dipole  
      pos         position magnetometers  
      ori         orientation magnetometers  
     
    See also CURRENT_DIPOLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/magnetic_dipole.m)
  """

  return Runtime.call("magnetic_dipole", *args, **kwargs)
