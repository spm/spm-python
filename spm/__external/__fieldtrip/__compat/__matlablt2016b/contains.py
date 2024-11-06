from spm.__wrapper__ import Runtime


def contains(*args, **kwargs):
    """
      CONTAINS True if text contains a pattern.  
          TF = contains(S,PATTERN) returns true if any element of string array S  
          contains PATTERN. TF is the same size as S.  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2016b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2016b/contains.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("contains", *args, **kwargs)
