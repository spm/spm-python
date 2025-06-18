from mpython import Runtime


def tbx_cfg_longitudinal(*args, **kwargs):
    """
      MATLABBATCH Configuration file for toolbox 'Longitudinal'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/tbx_cfg_longitudinal.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_longitudinal", *args, **kwargs)
