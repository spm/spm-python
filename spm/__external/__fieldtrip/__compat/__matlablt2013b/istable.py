from spm.__wrapper__ import Runtime


def istable(*args, **kwargs):
    """
      ISTABLE is a drop-in replacement for the same function that was  
        introduced in MATLAB R2013b.  
         
        In all MATLAB versions prior to 2013b this function returns false.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2013b/istable.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("istable", *args, **kwargs)
