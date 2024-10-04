from spm.__wrap__ import _Runtime


def _shiftpredict(*args, **kwargs):
  """  SHIFTPREDICT implements a shift-predictor for testing significance  
    of coherence within a single condition. This function is a subfunction   
    for SOURCESTATISTICS_SHIFTPREDICT and FREQSTATISTICS_SHIFTPREDICT.  
     
    cfg.method  
    cfg.numrandomization  
    cfg.method  
    cfg.method  
    cfg.loopdim  
    cfg.feedback  
    cfg.method  
    cfg.loopdim  
    cfg.correctm  
    cfg.tail  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/shiftpredict.m)
  """

  return _Runtime.call("shiftpredict", *args, **kwargs)
