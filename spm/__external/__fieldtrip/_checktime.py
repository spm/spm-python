from spm.__wrapper__ import Runtime


def _checktime(*args, **kwargs):
    """
      last input is always the required string  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/checktime.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("checktime", *args, **kwargs)
