from mpython import Runtime


def _ignorefields(*args, **kwargs):
    """
      IGNOREFIELDS returns a list of fields that can be present in the cfg structure that
        should be ignored at various places in the code, e.g. for provenance, history,
        size-checking, etc.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ignorefields.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ignorefields", *args, **kwargs)
