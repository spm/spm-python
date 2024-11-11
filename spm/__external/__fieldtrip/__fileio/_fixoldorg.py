from spm.__wrapper__ import Runtime


def _fixoldorg(*args, **kwargs):
    """
      FIXOLDORG use "old/new" instead of "org/new"  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fixoldorg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixoldorg", *args, **kwargs)
