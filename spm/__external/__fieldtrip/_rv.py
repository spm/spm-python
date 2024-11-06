from spm.__wrapper__ import Runtime


def _rv(*args, **kwargs):
    """
      RV returns the relative residual variance between measured and simulated data  
         
        rv = rv(measured, simulated)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rv", *args, **kwargs)
