from spm.__wrap__ import _Runtime


def _yokogawa2headmodel(*args, **kwargs):
  """  YOKOGAWA2HEADMODEL converts a spherical volume conductor model that can  
    be present in the header of a datafile into a structure that can  
    be used by FieldTrip.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/yokogawa2headmodel.m)
  """

  return _Runtime.call("yokogawa2headmodel", *args, **kwargs)
