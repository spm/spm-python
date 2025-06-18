from mpython import Runtime


def spm_combinations(*args, **kwargs):
    """
      FORMAT U = spm_combinations(Nu)
        Nu  - vector of dimensions
        U   - combinations of indices

        returns a matrix of all combinations of Nu
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_combinations.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_combinations", *args, **kwargs)
