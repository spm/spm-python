from spm.__wrapper__ import Runtime


def endsWith(*args, **kwargs):
    """
      ENDSWITH True if text starts with pattern.  
          TF = endsWith(S,PATTERN) returns true if any element of string array S  
          starts with PATTERN. TF is the same size as S.  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2016b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2016b/endsWith.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("endsWith", *args, **kwargs)
