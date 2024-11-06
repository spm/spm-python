from spm.__wrapper__ import Runtime


def getpid(*args, **kwargs):
    """
      GETPID returns the process identifier (PID) of the current Matlab  
        process.  
         
        Use as  
          num = getpid;  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/getpid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getpid", *args, **kwargs)
