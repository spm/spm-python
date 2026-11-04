from spm._runtime import Runtime


def getpid(*args, **kwargs):
    r"""
      GETPID returns the process identifier (PID) of the current MATLAB process  
         
        Use as  
          num = getpid  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/getpid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getpid", *args, **kwargs)
