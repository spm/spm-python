from spm.__wrap__ import _Runtime


def _combine_transform(*args, **kwargs):
  """  COMBINE_TRANSFORM combines the 4x4 homogenous transformation  
    matrices of the rotation, the scaling and the translation and  
    combines them in the desired order.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/combine_transform.m)
  """

  return _Runtime.call("combine_transform", *args, **kwargs)
