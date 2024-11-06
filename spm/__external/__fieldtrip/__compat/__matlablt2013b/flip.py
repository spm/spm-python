from spm.__wrapper__ import Runtime


def flip(*args, **kwargs):
    """
      FLIP is a drop-in replacement for the same function that was  
        introduced in MATLAB R2013b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2013b/flip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("flip", *args, **kwargs)
