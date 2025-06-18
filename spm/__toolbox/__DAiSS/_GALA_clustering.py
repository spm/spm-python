from mpython import Runtime


def _GALA_clustering(*args, **kwargs):
    """
    GALA_clustering is a function.
          res = GALA_clustering(lJcov, J1, S, distance, A)


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_clustering.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_clustering", *args, **kwargs)
