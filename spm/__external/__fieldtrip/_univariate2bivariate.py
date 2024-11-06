from spm.__wrapper__ import Runtime


def _univariate2bivariate(*args, **kwargs):
    """
      UNIVARIATE2BIVARIATE is a helper function for FT_CONNECTIVITYANALYSIS  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/univariate2bivariate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("univariate2bivariate", *args, **kwargs)
