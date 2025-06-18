from mpython import Runtime


def tbx_cfg_spatial(*args, **kwargs):
    """
      Configuration file for toolbox 'Spatial Tools'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/tbx_cfg_spatial.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_spatial", *args, **kwargs)
