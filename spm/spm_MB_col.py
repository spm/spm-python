from mpython import Runtime


def spm_MB_col(*args, **kwargs):
    """
      Return colours and marker size for number of partitions
        FORMAT [col,bol,msz] = spm_MB_col(n)
        n  - number of partitions
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_MB_col.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MB_col", *args, **kwargs)
