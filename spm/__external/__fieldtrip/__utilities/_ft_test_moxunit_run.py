from mpython import Runtime


def _ft_test_moxunit_run(*args, **kwargs):
    """
      FT_TEST_MOXUNIT_RUN documentation is included inside ft_test
        documentation.

        See also FT_TEST


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_moxunit_run.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_test_moxunit_run", *args, **kwargs)
