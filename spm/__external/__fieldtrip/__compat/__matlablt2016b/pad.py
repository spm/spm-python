from spm.__wrapper__ import Runtime


def pad(*args, **kwargs):
    """
      PAD adds leading or trailing characters, such as spaces, to the left or  
        right of an existing string.  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2016b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2016b/pad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pad", *args, **kwargs)
