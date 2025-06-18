from mpython import Runtime


def spm_cfg_deface(*args, **kwargs):
    """
      SPM Configuration file for toolbox 'De-Face'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_deface.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_deface", *args, **kwargs)
