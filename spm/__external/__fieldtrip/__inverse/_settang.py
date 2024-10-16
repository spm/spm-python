from spm.__wrapper__ import Runtime


def _settang(*args, **kwargs):
  """  set the dipole cartesian direction, given:  
    1) the instantenious decomposition vectors tanu and tanv  
    2) the instanteneous dipole orientation theta  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/settang.m)
  """

  return Runtime.call("settang", *args, **kwargs)
