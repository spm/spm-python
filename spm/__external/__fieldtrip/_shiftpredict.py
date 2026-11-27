from spm._runtime import Runtime


def _shiftpredict(*args, **kwargs):
    r"""
      SHIFTPREDICT implements a shift-predictor for testing significance  
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/shiftpredict.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("shiftpredict", *args, **kwargs)
