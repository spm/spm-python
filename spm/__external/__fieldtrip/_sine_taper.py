from mpython import Runtime


def _sine_taper(*args, **kwargs):
    """
      Compute Riedel & Sidorenko sine tapers.
        sine_taper(n, k) produces the first 2*k tapers of length n,
        returned as the columns of d.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/sine_taper.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sine_taper", *args, **kwargs)
