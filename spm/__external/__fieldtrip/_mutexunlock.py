from spm.__wrapper__ import Runtime


def _mutexunlock(*args, **kwargs):
    """
      MUTEXUNLOCK removes a lockfile  
         
        Use as  
          mutexunlock(lockfile)  
         
        See also MUTEXLOCK and http://en.wikipedia.org/wiki/Mutual_exclusion  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mutexunlock.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mutexunlock", *args, **kwargs, nargout=0)
