from mpython import Runtime


def test_spm_plot_ci(*args, **kwargs):
    """
      Unit Tests for spm_plot_ci
        Ensures that all the different plot types run without error
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_plot_ci.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_plot_ci", *args, **kwargs)
