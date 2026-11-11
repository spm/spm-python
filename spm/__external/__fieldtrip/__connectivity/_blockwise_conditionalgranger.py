from spm._runtime import Runtime


def _blockwise_conditionalgranger(*args, **kwargs):
    r"""
      BLOCKWISE_CONDITIONALGRANGER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/blockwise_conditionalgranger.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("blockwise_conditionalgranger", *args, **kwargs)
