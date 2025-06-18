from mpython import Runtime


def _ft_test_update_dependency(*args, **kwargs):
    """
      FT_TEST_UPDATE_DEPENDENCY documentation is included inside ft_test
        documentation.

        See also FT_TEST, READLINES, WRITELINES


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_update_dependency.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_test_update_dependency", *args, **kwargs, nargout=0)
