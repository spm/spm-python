from mpython import Runtime


def spm_cfg_disp(*args, **kwargs):
    """
      SPM Configuration file for Image Display
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_disp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_disp", *args, **kwargs)
