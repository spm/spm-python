from mpython import Runtime


def _standardise(*args, **kwargs):
    """
      STANDARDISE computes the zscore of a matrix along dimension dim
        has similar functionality as the stats-toolbox's zscore function

        Use as
          x = standardise(x, dim)

        See also ZSCORE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/standardise.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("standardise", *args, **kwargs)
