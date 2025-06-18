from mpython import Runtime


def _ft_test_untested_functions(*args, **kwargs):
    """
      FT_TEST_UNTESTED_FUNCTIONS documentation is included inside ft_test
        documentation.

        See also FT_TEST


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_untested_functions.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_test_untested_functions", *args, **kwargs, nargout=0)
