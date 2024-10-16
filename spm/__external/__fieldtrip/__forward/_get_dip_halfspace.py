from spm.__wrapper__ import Runtime


def _get_dip_halfspace(*args, **kwargs):
  """  GET_DIP_HALFSPACE checks if the dipole is in the empty halfspace and  
    returns true if this happens. The normal of the plane points by  
    convention to the empty halfspace.  
            
    is_in_empty = get_dip_halfspace(P,vol);  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/get_dip_halfspace.m)
  """

  return Runtime.call("get_dip_halfspace", *args, **kwargs)
