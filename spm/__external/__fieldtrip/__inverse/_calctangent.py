from spm._runtime import Runtime


def _calctangent(*args, **kwargs):
    r"""
      Based on calcrads.m, only difference is that RDip is alread  
        with respect to the sphere origin in calctangent.m  
        MODIFIED 13th JAN 2005 MATT BROOKES  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/inverse/private/calctangent.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("calctangent", *args, **kwargs)
