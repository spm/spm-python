from mpython import Runtime


def _keyvalcheck(*args, **kwargs):
    """
      KEYVALCHECK is a helper function for parsing optional key-value input pairs.

        Use as
          keyvalcheck(argin, 'required',  {'key1', 'key2', ...})
          keyvalcheck(argin, 'forbidden', {'key1', 'key2', ...})
          keyvalcheck(argin, 'optional',  {'key1', 'key2', ...})

        See also KEYVAL


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/keyvalcheck.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keyvalcheck", *args, **kwargs, nargout=0)
