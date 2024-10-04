from spm.__wrap__ import _Runtime


def _volumeedit(*args, **kwargs):
  """  VOLUMEEDIT allows for editing of a (booleanized) volume, in order to  
    remove unwanted voxels. Interaction proceeds with the keyboard and the  
    mouse.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeedit.m)
  """

  return _Runtime.call("volumeedit", *args, **kwargs)
