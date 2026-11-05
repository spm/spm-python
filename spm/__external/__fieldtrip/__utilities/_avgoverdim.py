from spm._runtime import Runtime


def _avgoverdim(*args, **kwargs):
    r"""
    avgoverdim is a function.  
          data = avgoverdim(data, avgdim, fb)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/avgoverdim.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("avgoverdim", *args, **kwargs)
