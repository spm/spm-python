from mpython import Runtime


def _fwer(*args, **kwargs):
    """
      FWER family-wise error rate control using Bonferoni method

        Use as
          h = fwer(p, q)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fwer.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fwer", *args, **kwargs)
