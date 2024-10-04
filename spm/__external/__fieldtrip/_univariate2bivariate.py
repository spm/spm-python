from spm.__wrap__ import _Runtime


def _univariate2bivariate(*args, **kwargs):
  """  UNIVARIATE2BIVARIATE is a helper function for FT_CONNECTIVITYANALYSIS  
     
    Use as  
      [data, powindx, hasrpt] = univariate2bivariate(data, inparam, outparam, dtype, ...)  
    where  
      data        = FieldTrip structure according to dtype (see below)  
      inparam     = string  
      outparam    = string  
      dtype       = string, can be 'freq', 'source', 'raw'  
    and additional options come in key-value pairs and can include  
      channelcmb  =   
      demeanflag  =   
      keeprpt     =   
      sqrtflag    =  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/univariate2bivariate.m)
  """

  return _Runtime.call("univariate2bivariate", *args, **kwargs)
