from spm.__wrap__ import _Runtime


def _raw2data(*args, **kwargs):
  """  RAW2DATA is a helper function that converts raw data to various types of  
    averages. This function is used to apply the analysis steps that were  
    written for use on preprocessed data also on averaged data.  
     
    This function is the counterpart of DATA2RAW and is used in MEGREALIGN, MEGPLANAR, MEGREPAIR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/raw2data.m)
  """

  return _Runtime.call("raw2data", *args, **kwargs)
