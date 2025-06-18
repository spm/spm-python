from mpython import Runtime


def spm_cfg_opm_synth_gradiometer(*args, **kwargs):
    """
      Configuration file for performing synthetic gradiometery on OPM data
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_opm_synth_gradiometer.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_opm_synth_gradiometer", *args, **kwargs)
