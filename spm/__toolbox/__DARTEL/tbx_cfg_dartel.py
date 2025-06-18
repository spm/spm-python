from mpython import Runtime


def tbx_cfg_dartel(*args, **kwargs):
    """
      Configuration file for toolbox 'Dartel Tools'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/tbx_cfg_dartel.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_dartel", *args, **kwargs)
