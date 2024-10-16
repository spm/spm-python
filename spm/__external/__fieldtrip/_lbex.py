from spm.__wrapper__ import Runtime


def _lbex(*args, **kwargs):
  """  This function will add the field "subspace" to the sourcemodel definition.  
     
    The subspace projection is based on the LBEX (local basis expansion)  
    method.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/lbex.m)
  """

  return Runtime.call("lbex", *args, **kwargs)
