from spm.__wrap__ import _Runtime


def _write_brainvoyager(*args, **kwargs):
  """  helper function to write volumetric data for brainvoyager.  
    this is old code that moved from ft_volumewrite to clean up  
    the high level function a bit. it is assumed that the orientation  
    of the volume is correct.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_brainvoyager.m)
  """

  return _Runtime.call("write_brainvoyager", *args, **kwargs, nargout=0)
