from spm._runtime import Runtime


def dpss(*args, **kwargs):
    r"""
      DPSS approximate the discrete prolate spheroidal (DPSS), or Slepian sequences  
        using a precomputed version on disk  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/signal/dpss_hack/dpss.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dpss", *args, **kwargs)
