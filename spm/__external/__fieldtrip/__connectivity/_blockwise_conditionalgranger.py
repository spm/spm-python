from mpython import Runtime


def _blockwise_conditionalgranger(*args, **kwargs):
    """
      BLOCKWISE_CONDITIONALGRANGER


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/blockwise_conditionalgranger.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("blockwise_conditionalgranger", *args, **kwargs)
