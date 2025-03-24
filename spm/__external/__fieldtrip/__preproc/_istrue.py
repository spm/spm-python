from mpython import Runtime


def _istrue(*args, **kwargs):
    """
      ISTRUE converts an input argument like "yes/no", "true/false" or "on/off" into a
        boolean. If the input is boolean, then it will remain like that.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/private/istrue.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("istrue", *args, **kwargs)
