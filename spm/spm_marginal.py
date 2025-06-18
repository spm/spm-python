from mpython import Runtime


def spm_marginal(*args, **kwargs):
    """
      Marginal densities over a multidimensional array of probabilities
        FORMAT [Y] = spm_marginal(X)
        X  - numeric array of probabilities

        Y  - cell array of marginals

        See also: spm_dot
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_marginal.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_marginal", *args, **kwargs)
