from spm.__wrap__ import _Runtime


def _fixcoordsys(*args, **kwargs):
  """  FIXCOORDSYS ensures that the coordinate system is consistently  
    described. E.g. SPM and MNI are technically the same coordinate  
    system, but the strings 'spm' and 'mni' are different.  
     
    See also FT_DETERMINE_COORDSYS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/fixcoordsys.m)
  """

  return _Runtime.call("fixcoordsys", *args, **kwargs)
