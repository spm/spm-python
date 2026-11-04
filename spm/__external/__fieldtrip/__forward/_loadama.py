from spm._runtime import Runtime


def _loadama(*args, **kwargs):
    r"""
      LOADAMA read an inverted A-matrix and associated geometry information  
        from an ama file that was written by Tom Oostendorp's DIPOLI  
         
        Use as  
          [ama] = loadama(filename)  
         
        See also LOADTRI, LOADMAT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/loadama.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadama", *args, **kwargs)
