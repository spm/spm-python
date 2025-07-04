from spm._runtime import Runtime


def spm_log(*args, **kwargs):
    """
      Log of numeric array plus a small constant  
        FORMAT A = spm_log(A)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_log.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_log", *args, **kwargs)
