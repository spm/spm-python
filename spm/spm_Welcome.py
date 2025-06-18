from mpython import Runtime


def spm_Welcome(*args, **kwargs):
    """
      Open SPM's welcome splash screen
        FORMAT F = spm_Welcome
        F        - welcome figure handle
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Welcome.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Welcome", *args, **kwargs)
