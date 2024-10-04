from spm.__wrap__ import _Runtime


def _volumeflip(*args, **kwargs):
  """  VOLUMEFLIP  
     
    See also VOLUMEPERMUTE, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeflip.m)
  """

  return _Runtime.call("volumeflip", *args, **kwargs)
