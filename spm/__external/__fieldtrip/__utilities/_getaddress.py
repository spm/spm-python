from mpython import Runtime


def _getaddress(*args, **kwargs):
    """
      GETADDRESS returns the IP address

        Use as
          address = getaddress();
        or
          address = getaddress(hostname);

        See also GETUSERNAME, GETHOSTNAME


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getaddress.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getaddress", *args, **kwargs)
