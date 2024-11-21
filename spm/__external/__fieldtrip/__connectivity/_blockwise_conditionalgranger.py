from spm.__wrapper__ import Runtime


def _blockwise_conditionalgranger(*args, **kwargs):
    """
      BLOCKWISE_CONDITIONALGRANGER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/blockwise_conditionalgranger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("blockwise_conditionalgranger", *args, **kwargs)
