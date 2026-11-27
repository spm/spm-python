from spm._runtime import Runtime


def precompute_dpss(*args, **kwargs):
    r"""
      assume 1 second and 1000 Hz sampling rate  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/signal/dpss_hack/precompute_dpss.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("precompute_dpss", *args, **kwargs)
