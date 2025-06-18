from mpython import Runtime


def spm_create_vol(*args, **kwargs):
    """
      Create a NIfTI image volume
        FORMAT V = spm_create_vol(V)
        V        - image volume information (see spm_vol.m)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_create_vol.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_create_vol", *args, **kwargs)
