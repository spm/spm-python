from spm.__wrap__ import _Runtime


def _volumepermute(*args, **kwargs):
  """  VOLUMEPERMUTE  
     
    See also VOLUMEFLIP, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumepermute.m)
  """

  return _Runtime.call("volumepermute", *args, **kwargs)
