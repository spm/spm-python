from spm._runtime import Runtime


def _checkchan(*args, **kwargs):
    """
      last input is always the required string  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/checkchan.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("checkchan", *args, **kwargs)
