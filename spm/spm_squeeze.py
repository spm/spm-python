from mpython import Runtime


def spm_squeeze(*args, **kwargs):
    """
      Version of squeeze with the possibility to select the dimensions to remove
        FORMAT  B = spm_squeeze(A, dim)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_squeeze.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_squeeze", *args, **kwargs)
