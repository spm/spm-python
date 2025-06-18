from mpython import Runtime


def _selparam(*args, **kwargs):
    """
      SELPARAM(DATA) extracts the fieldnames param of the structure data containing functional
        data, which have a dimensionality consistent with the dimord field in the data. Selparam
        is a helper function to selectdata


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/selparam.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("selparam", *args, **kwargs)
