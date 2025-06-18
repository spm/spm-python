from mpython import Runtime


def spm_hilbert(*args, **kwargs):
    """
      Computes analytic signal
        FORMAT [x] = spm_hilbert(xr)

        Returns analytic signal x = xr + i*xi such that xi is the Hilbert
        transform of real vector xr.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hilbert.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_hilbert", *args, **kwargs)
