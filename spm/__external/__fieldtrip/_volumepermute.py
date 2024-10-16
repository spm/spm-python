from spm.__wrapper__ import Runtime


def _volumepermute(*args, **kwargs):
  """  VOLUMEPERMUTE  
     
    See also VOLUMEFLIP, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumepermute.m)
  """

  return Runtime.call("volumepermute", *args, **kwargs)
