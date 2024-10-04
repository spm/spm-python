from spm.__wrap__ import _Runtime


def _halfspace_medium_leadfield(*args, **kwargs):
  """  HALFSPACE_MEDIUM_LEADFIELD calculate the halfspace medium leadfield  
    on positions pnt for a dipole at position rd and conductivity cond  
    The halfspace solution requires a plane dividing a conductive zone of  
    conductivity cond, from a non coductive zone (cond = 0)  
            
    [lf] = halfspace_medium_leadfield(rd, elc, cond)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/halfspace_medium_leadfield.m)
  """

  return _Runtime.call("halfspace_medium_leadfield", *args, **kwargs)
