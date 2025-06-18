from mpython import Runtime


def tbx_cfg_render(*args, **kwargs):
    """
      Configuration file for toolbox 'Rendering'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SRender/tbx_cfg_render.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_render", *args, **kwargs)
