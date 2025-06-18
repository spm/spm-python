from mpython import Runtime


def tbx_cfg_tsss(*args, **kwargs):
    """
      Configuration file for toolbox 'TSSS'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/tbx_cfg_tsss.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_tsss", *args, **kwargs)
