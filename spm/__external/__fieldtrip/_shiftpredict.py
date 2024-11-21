from spm.__wrapper__ import Runtime


def _shiftpredict(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/shiftpredict.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("shiftpredict", *args, **kwargs)
