from spm.__wrapper__ import Runtime


def _mutexlock(*args, **kwargs):
    """
      MUTEXLOCK creates a lockfile, or if it already exists, waits until  
        another process removes the lockfile and then creates it. This function  
        can be used for "mutual exclusion", i.e. executing multiple processes in  
        parallel where part of the processing is not allowed to run  
        simultaneously.  
         
        Use as  
          mutexlock(lockfile, timeout)  
         
        See also MUTEXUNLOCK and http://en.wikipedia.org/wiki/Mutual_exclusion  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mutexlock.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mutexlock", *args, **kwargs, nargout=0)
