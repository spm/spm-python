from spm.__wrap__ import _Runtime


def _isplottingfunction(*args, **kwargs):
  """  ISPLOTTINGFUNCTION is a helper function for reproducescript, and  
    is used for the cfg.reproducescript functionality. It compares the input  
    function name with the list of known FieldTrip plotting functions and  
    returns 1 if it is a plotting function, and 0 otherwise.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/isplottingfunction.m)
  """

  return _Runtime.call("isplottingfunction", *args, **kwargs)
