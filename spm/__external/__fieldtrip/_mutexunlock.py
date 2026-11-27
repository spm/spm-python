from spm._runtime import Runtime


def _mutexunlock(*args, **kwargs):
    r"""
      MUTEXUNLOCK removes a lockfile  
         
        Use as  
          mutexunlock(lockfile)  
         
        See also MUTEXLOCK and http://en.wikipedia.org/wiki/Mutual_exclusion  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/mutexunlock.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mutexunlock", *args, **kwargs, nargout=0)
