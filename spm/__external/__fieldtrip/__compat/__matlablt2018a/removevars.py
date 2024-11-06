from spm.__wrapper__ import Runtime


def removevars(*args, **kwargs):
    """
      T2 = removevars(T1,vars) deletes the table variables specified  
        by vars and copies the remaining variables to T2 (see diagram). You  
        can specify variables by name, by position, or using logical indices.  
         
        Use as  
          T2 = removevars(T1, vars)  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2018a.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2018a/removevars.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("removevars", *args, **kwargs)
