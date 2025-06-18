from mpython import Runtime


def spm_dcm_compare(*args, **kwargs):
    """
      Compare two or more estimated models
        FORMAT spm_dcm_compare(P)

        P  - a char or cell array of DCM filenames
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_compare.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_compare", *args, **kwargs, nargout=0)
