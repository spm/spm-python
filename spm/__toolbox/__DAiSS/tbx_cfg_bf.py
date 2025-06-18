from mpython import Runtime


def tbx_cfg_bf(*args, **kwargs):
    """
      Configuration file for toolbox 'Beamforming'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/tbx_cfg_bf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_bf", *args, **kwargs)
